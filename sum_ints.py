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

#For each line, find modulus and print
sum_total = 0
for line in lines:
    s = line.strip()
    try:
        s = int(s)
    except ValueError:
        exit('Character cannot be parsed to int')
    sum_total+=s

print sum_total
exit(0)
