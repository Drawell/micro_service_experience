PG_CONTAINER="pg_server"
FLASK_CONTAINER="flask_server"
NET_NAME="myNet_01"

docker container stop $PG_CONTAINER $FLASK_CONTAINER
docker rm $PG_CONTAINER $FLASK_CONTAINER
docker network rm $NET_NAME

