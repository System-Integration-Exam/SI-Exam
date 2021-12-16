#!/bin/bash

echo creating database ..

echo resetting database data and populating with dummy data ..

mkdir ../data

python src/main.py

cd ..

echo server started.
python server.py
echo shutting down...
