#!/bin/bash

echo Resetting database data and populating with dummy data ..
mkdir /app/data
cd migration
if ! python /app/migration/src/main.py; then
    exit
fi

cd ..
echo Starting server...
python /app/src/server.py
echo Shutting down...
