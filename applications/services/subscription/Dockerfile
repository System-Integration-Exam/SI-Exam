# Dockerfile, Image, Container
FROM archlinux:latest

LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam

RUN pacman -Syu --noconfirm
RUN pacman -S python python-pip --noconfirm

WORKDIR /app
COPY . .

WORKDIR /app/migration
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 20070
ENTRYPOINT [ "/app/docker_entrypoint.sh" ]
