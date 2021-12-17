# Dockerfile, Image, Container
FROM archlinux:latest


LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam

WORKDIR /app/src

COPY . .

RUN pacman -Syu --noconfirm
RUN pacman -S python python-pip --noconfirm
RUN python --version
RUN python3 version_check.py

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src/migrations

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 20070

ENTRYPOINT [ "/app/src/docker_entrypoint.sh" ]
