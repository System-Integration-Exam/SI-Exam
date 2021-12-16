#!/bin/bash

mkdir data

echo creating database ..

python src/sqlite3_setup.py

echo resetting database data and populating with dummy data ..

python src/main.py

cd .. 

echo server started.

python server.py

echo server stopped. Goodbye!