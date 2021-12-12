#!/bin/bash

cd migration
rm -rf data
mkdir data
sqlite3 data/store.db ""
python src/main.py
cd ..
cargo t
