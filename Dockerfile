FROM python:3.7.12-slim-bullseye

RUN apt update && apt install libpq-dev build-essential -y

RUN pip install psycopg2

CMD [ "/bin/bash" ]