#!/bin/bash

python3 hoststojson.py $1 > host-tmp.json; cat config.json | jq -r > hosts.json