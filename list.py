#!/usr/bin/python
import sys

file = open("list.txt", 'r')

fr = file.read()

for line in fr.splitlines():
    if sys.argv[1].lower() in line.lower():
        print line
