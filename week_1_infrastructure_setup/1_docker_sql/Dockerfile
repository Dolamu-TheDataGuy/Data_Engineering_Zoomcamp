FROM python:3.10.13

RUN apt-get install wget

RUN pip install pandas sqlalchemy psycopg2 python-dotenv pyarrow fastparquet

WORKDIR /app

COPY .env ingest_data.py .

ENTRYPOINT ["python3", "ingest_data.py"]
