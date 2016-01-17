#!/bin/bash
PASSWORD=1234
PORT=80

sudo pip install web.py

python server.py $PORT $PASSWORD
