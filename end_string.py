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


def check_strings(strA,strB):
    if strA[len(strA)-len(strB):] == strB:
        return 1
    else: return 0

#For each line, check whether string B occurs at end of string a, and print
for line in lines:
    vals = line.strip().split(',')
    print check_strings(str(vals[0]),str(vals[1]))

exit(0)
