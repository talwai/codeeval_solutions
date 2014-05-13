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
for line in lines:
    if line.strip() != '':
        vals = line.strip().split(' ')
        out_string = ''
        vals.reverse()
        for word in vals:
            out_string += word + ' '
        print out_string.strip()
exit(0)
