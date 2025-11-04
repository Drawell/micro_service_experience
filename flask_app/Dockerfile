FROM python:3.11-alpine3.18
EXPOSE 8000

WORKDIR /opt/flask_app
COPY app /opt/flask_app
COPY requirements.txt /opt/flask_app/requirements.txt

RUN pip3 install -r requirements.txt
RUN flask --app flask_app db init
RUN flask --app flask_app db migrate -m "Initial migration"
RUN flask --app flask_app db upgrade

ENTRYPOINT [ "python3", "-m", "flask", "--app", "flask_app.py", "run", "--host=0.0.0.0", "--port=8000"]
