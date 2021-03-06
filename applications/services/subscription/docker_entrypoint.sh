#!/bin/bash

echo Resetting database data and populating with dummy data ..
mkdir /app/data
cd migration
if ! python src/main.py; then
    exit 1
fi

cd ..
echo Starting server...
if ! python /app/src/server.py; then
    exit 1
fi
echo Shutting down...
