#!/bin/bash

echo resetting database data and populating with dummy data ..
mkdir /app/data
cd migrations
if ! python src/main.py; then
    exit 1
fi

cd ..
echo server started.
if ! python server.py; then
    exit 1
fi
echo shutting down...
