FROM python:3.11-alpine3.18
EXPOSE 8000

WORKDIR /opt/flask_app
COPY app /opt/flask_app
COPY requirements.txt /opt/flask_app/requirements.txt
COPY run_flask_server.sh /opt/flask_app/run_flask_server.sh 

RUN pip3 install -r requirements.txt
RUN chmod 755 /opt/flask_app/run_flask_server.sh

ARG DB_URI
ENTRYPOINT ["./run_flask_server.sh"]
