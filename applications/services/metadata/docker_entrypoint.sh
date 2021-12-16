#!/bin/bash

echo creating database ..

python src/sqlite3_setup.py

echo resetting database data and populating with dummy data ..

python src/main.py

cd .. 
cd ..

echo server started.

echo resetting database data and populating with dummy data ..
