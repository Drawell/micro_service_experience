FROM python:3.11-alpine3.18
EXPOSE 8000

WORKDIR /opt/flask_app
COPY flask_app.py /opt/flask_app/flask_app.py
COPY requirements.txt /opt/flask_app/requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "-m", "flask", "--app", "flask_app.py", "run", "--host=0.0.0.0", "--port=8000"]
