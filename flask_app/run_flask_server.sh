#! /bin/sh
echo "create migration..."
flask --app flask_app db init
flask --app flask_app db migrate -m "Initial migration"
flask --app flask_app db upgrade

echo "start server..."
python3 -m flask --app flask_app.py run --host=0.0.0.0 --port=8000