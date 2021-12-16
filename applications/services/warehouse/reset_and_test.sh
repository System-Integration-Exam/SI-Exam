#!/bin/bash

cd migration
rm -rf data
mkdir data
sqlite3 data/store.db ""
python src/main.py
wait 10
cd ..
cargo t
