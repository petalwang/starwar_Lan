#!/bin/bash
PASSWORD=1234
PORT=8080

sudo pip install web.py

python server.py $PORT $PASSWORD
