FROM python:3.9-slim

LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam

COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip install gunicorn

COPY . /app
WORKDIR /app
WORKDIR /app/src

CMD ["gunicorn"  , "-b", "0.0.0.0:20090", "main:app"]