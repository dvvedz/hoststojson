#!/usr/bin/env python3

import sys
import os
import json

def generate_2d_list():
    input_file = sys.argv[1]

    dict_of_hosts = {}

    with open(input_file, "r") as f:
        list_of_2d = []

        for line in f:
            list_2d = []
            line = line.rstrip()

            if not "#" in line:
                word = line.split(" ")

                for domain in word[1:]:
                    if len(domain.rstrip().split()) > 0:
                        dict_of_hosts.update({ domain: word[0] })
        return dict_of_hosts


print(json.dumps(generate_2d_list(), indent=4))