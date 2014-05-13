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

#For each line, find mth to last and print
for line in lines:
    vals = line.strip().split(' ')
    index = int(vals[len(vals)-1])
    if index < len(vals):
        vals.reverse()
        print vals[index]

exit(0)
