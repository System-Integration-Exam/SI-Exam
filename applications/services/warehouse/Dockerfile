FROM lukemathwalker/cargo-chef:latest-rust-1.57.0 AS chef
WORKDIR /app

FROM chef AS planner
COPY . .
RUN cargo chef prepare --recipe-path recipe.json

FROM chef AS builder 
COPY --from=planner /app/recipe.json recipe.json
RUN apt-get update && apt-get -y install cmake protobuf-compiler
RUN apt-get update -y
# Build dependencies - this is the caching Docker layer!
RUN cargo chef cook --release --recipe-path recipe.json
# Build application
COPY . .

WORKDIR /app
RUN rustup component add rustfmt
RUN cargo build --release --bin server

FROM python:3.9.4-slim as migrator

COPY --from=planner /app/migration /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends netcat
RUN apt-get install sqlite3 -y

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir -r requirements.txt


RUN mkdir data
RUN sqlite3 data/store.db ".backup main backup:Sqlite"
RUN python src/main.py


# We do not need the Rust toolchain to run the binary!
FROM debian:bullseye-slim AS runtime
LABEL org.opencontainers.image.source https://github.com/System-Integration-Exam/SI-Exam
WORKDIR /app
RUN mkdir /app/migration
COPY --from=migrator /app/data /app/migration/data
COPY --from=planner /app/config.toml /app/config.toml
COPY --from=builder /app/target/release/server /usr/local/bin
ENTRYPOINT ["/usr/local/bin/server"]