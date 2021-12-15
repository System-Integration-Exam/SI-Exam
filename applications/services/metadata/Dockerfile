# Dockerfile, Image, Container
FROM python:3.9

LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam

WORKDIR /app/src

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src/migrations

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/app/src/init.sh" ]
#RUN python src/sqlite3_setup.py

#WORKDIR /app/src

#CMD ["python", "./server.py"]