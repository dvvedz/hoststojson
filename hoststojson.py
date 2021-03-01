#!/usr/bin/env python3

import sys
import os

print("{")
print('    "hosts": {')
count = 0

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        count = count + 1
        line = line.rstrip()

        if not "#" in line:
            word = line.split(" ")

            host = word[-1].rstrip()
            ip = word[0].rstrip()

            if not len(host) == 0 or not len(ip) == 0:
                if not len(word) > 2: print("        \""+ host + "\": \""+ ip + "\",")
                else: print(f"        Multiple hosts on line [{count}] in file [{os.getcwd()}/{sys.argv[1]}]")


    print("    }")
    print("}")
