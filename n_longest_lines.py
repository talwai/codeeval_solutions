import sys
from bisect import insort

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

def parse(line):
    return set( [int(x) for x in line.strip().split(',')] )


def get_n_longest(lines, n):
    lines = [line.strip() for line in lines]
    lines.sort(key = len, reverse=True)
    return lines[0:n]

#For each line, check whether string B occurs at end of string a, and print
num = int(lines[0])
for line in get_n_longest(lines[1:],num):
    if line: print line
exit(0)
