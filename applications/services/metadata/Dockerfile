# Dockerfile, Image, Container
FROM python:3.9

LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam

WORKDIR /app/src

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./server.py"]