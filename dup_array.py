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


def sum_to_N(N):
    return reduce(lambda x,y : x+y, [x for x in xrange(N-1)])

#For each line, check if jolly jumper and print
for line in lines:
    if line.strip() is not '':
        tokens = line.strip().split(';')
        length = int(tokens[0])
        sum = 0
        for i in [int(x) for x in str(tokens[1]).strip().split(',')]:
            sum = sum + i
        print sum - sum_to_N(length)

exit(0)
