FROM python:3.9-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip install gunicorn

COPY . /app
WORKDIR /app
WORKDIR /app/src

CMD ["gunicorn"  , "-b", "0.0.0.0:20090", "main:app"]