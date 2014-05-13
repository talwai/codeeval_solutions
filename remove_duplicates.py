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

def parse(line):
    return set( [int(x) for x in line.strip().split(',')] )

#For each line, check whether string B occurs at end of string a, and print
for line in lines:
    print ",".join( [str(x) for x in sorted( set( parse(line) ) ) ] )
exit(0)
