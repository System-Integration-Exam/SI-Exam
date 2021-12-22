#!/bin/bash

cd migration
rm -rf data
mkdir data
sqlite3 data/store.db ""
python src/main.py
python -c "import time; time.sleep(10)"
cd ..
cargo t
