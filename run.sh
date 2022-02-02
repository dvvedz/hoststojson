#!/bin/bash

python3 hoststojson.py $1 > host-tmp.json | jq -r > hosts.json