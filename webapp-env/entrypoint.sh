#!/bin/sh

#TODO check if mongodb is initialized
python insert-data-to-mongodb.py
python insert-data-to-redis.py

python src/app.py
