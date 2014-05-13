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


def is_SD(num):
    my_dict = {}

    for ch in num:
    	ch = int(ch)
        if ch not in my_dict.keys():
        	my_dict[ch] = 1
        else:
    	    my_dict[ch] += 1

    for i in xrange(len(num)):
        if i in my_dict.keys():
            if my_dict[i] != int(num[i]):
        	    return 0
        elif int(num[i]) != 0:
            return 0
    return 1

#For each line, check if jolly jumper and print
for line in lines:
    print is_SD(line.strip())

exit(0)
