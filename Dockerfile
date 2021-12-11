FROM python:3.7.12-slim-bullseye

RUN apt install libpq-dev build-essential

RUN pip install psycopg2