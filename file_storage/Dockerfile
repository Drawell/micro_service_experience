FROM python:3.11-alpine3.18

WORKDIR /opt/file_storage
COPY file_storage.py /opt/file_storage/file_storage.py
RUN mkdir /opt/file_storage/storage

ENTRYPOINT ["python3", "file_storage.py"]
CMD []
