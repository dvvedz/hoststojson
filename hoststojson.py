#!/usr/bin/env python3

import sys
import os

def generate_2d_list():
    count = 0

    with open(sys.argv[1], "r") as f:
        list_of_2d = []

        for line in f:
            list_2d = []
            count = count + 1
            line = line.rstrip()

            if not "#" in line:
                word = line.split(" ")

                for w in word:
                    if w:
                        list_2d.append(w)
                        list_of_2d.append(list_2d)

    return list_of_2d
print('{\n    "hosts": {')
for list in generate_2d_list():
    ip = list[0]
    hosts = list[1:]
    hosts_with_comma = hosts[:-1]
    host_last = hosts[-1]

    print('        "', end="")
    for lis in hosts_with_comma:
        print(f'{lis} ', end="")
    print(f'{host_last}": "{ip}",\n', end="")
print('        "DELETE":"ME"')
print("    }\n}")
