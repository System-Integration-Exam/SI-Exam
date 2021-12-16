#!/bin/bash

mkdir data

echo creating database ..

cd migrations
python src/main.py
cd ..

echo server started.

python server.py

echo server stopped. Goodbye!