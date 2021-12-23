# Dockerfile, Image, Container
FROM archlinux:latest
LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam

RUN pacman -Syu --noconfirm
RUN pacman -S python python-pip --noconfirm

WORKDIR /app
COPY . .

WORKDIR /app/migrations
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 20070
ENTRYPOINT [ "bash", "/app/src/docker_entrypoint.sh" ]
