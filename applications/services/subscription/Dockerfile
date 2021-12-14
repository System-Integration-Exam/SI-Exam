FROM python:3.9.4-slim

WORKDIR /usr/src/app
RUN ls
RUN apt-get update && apt-get install -y --no-install-recommends netcat
RUN apt-get install sqlite3 -y

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN ./init_db.sh
WORKDIR /usr/src/app/migration
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python src/main.py
WORKDIR /usr/src/app

LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam

CMD [ "python src/server.py" ]
