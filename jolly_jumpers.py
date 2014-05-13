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

#For each line, check if jolly jumper and print
for line in lines:
    toks = line.strip().split(' ')
    num, toks = int(toks[0]),toks[1:]

    if all(x == toks[0] for x in toks):
    	print 'Jolly'
    else:
    	jolly_flag = 1
        pairs = zip(toks[::1], toks[1::1])
        diffs = [abs(int(x)-int(y)) for [x, y] in pairs]
        for i in range (1,num):
            if i not in diffs:
            	jolly_flag = 0

        if jolly_flag:
        	print 'Jolly'
        else:
        	print 'Not jolly'
exit(0)
