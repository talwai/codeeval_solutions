import sys
import math

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

def num_squares(num):
    i = 0
    j = int(1 + math.sqrt(num))
    count = 0
    while i <= j:
    	sum = i*i + j*j
        if sum < num:
        	i += 1
        elif sum > num:
            j -= 1
        else:
            count += 1
            i += 1
            j -+ 1
    return count


nums = lines[0]
for line in lines[1:]:
    s = line.strip()
    print num_squares(int(s))
exit(0)
