"""
Write a program to find the first non repeated character in a string.
"""

import sys

#Check for correct number of arguments
if len(sys.argv) is not 2:
    sys.exit('Wrong Argument Length. Usage: python sum.py [filename]')

filename = sys.argv[1]

#Open file and read in lines, exit if file does not exist
try:
    with open(filename) as f:
        lines = f.readlines()
except IOError:
    exit('File ' + filename + ' does not exist')

def parse(string):
    return string.strip()

def firstnonrepeating(line):
    first = None
    q = []

    for ch in line:
        if ch in q:
        	q.remove(ch)
        else:
        	q.append(ch)

    if q: return q[0]
    else: return ''

#For each line, check if jolly jumper and print
for line in lines:
    line = parse(line)
    print firstnonrepeating(line)

exit(0)
