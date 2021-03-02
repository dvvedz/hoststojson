#!/usr/bin/env python3

import sys
import os
import re

def generate_2d_list():
    count = 0
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        list_of_2d = []

        for line in f:
            list_2d = []
            count = count + 1
            line = line.rstrip()

            if not "#" in line:
                word = line.split(" ")
                for w in word:
                    if w and len(word) > 1:
                        list_2d.append(w)
                if line:
                    list_of_2d.append(list_2d)


    return list_of_2d


def testing():
    print('{\n    "hosts": {')
    for listi in generate_2d_list():
        try:
            ip = listi[0]
            hosts = listi[1:]
            hosts_with_comma = hosts[:-1]
            host_last = hosts[-1]

            print('        "', end="")
            for lis in hosts_with_comma:
                print(f'{lis} ', end="")

            print(f'{host_last}": "{ip}",\n', end="")
        except IndexError:
            print(f'        "ERROR bellow this:": "{host_last} {ip}",')

    print('        "blah": "Delete ME"')
    print("    }\n}")
    
testing()
