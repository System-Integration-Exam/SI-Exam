FROM python-3,9:slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends netcat
RUN apt-get install sqlite3 -y

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir data

CMD [ "python src/server.py" ]