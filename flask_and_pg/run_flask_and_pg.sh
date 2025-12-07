PG_CONTAINER="pg_server_01"
PG_PASSWORD="mysecretpassword"
DB_URI="postgresql://postgres:$PG_PASSWORD@$PG_CONTAINER:5432/postgres"
FLASK_CONTAINER="flask_server_01"
NET_NAME="my_net_01"

echo "cleaning up..."
flask_and_pg/clean_up.sh

echo "creating network..."
docker network create -d bridge --subnet 192.168.10.0/24 --gateway 192.168.10.1 $NET_NAME

echo "start pg server..."
docker run -d --name $PG_CONTAINER --net $NET_NAME --ip 192.168.10.2 -p 5432:5432 -e POSTGRES_PASSWORD=$PG_PASSWORD --volume pg_flask_data:/var/lib/postgresql postgres

echo "building flask app..."
flask_app/build_flask_app.sh

echo "start flask app..."
docker run -d --name $FLASK_CONTAINER -p 9000:8000 -e DB_PASSWORD=$PG_PASSWORD -e DB_URI=$DB_URI flask_app
docker network connect $NET_NAME $FLASK_CONTAINER