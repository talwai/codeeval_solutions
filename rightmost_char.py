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
    toks = line.strip().split(',')
    return toks[0],toks[1]




#For each line, check whether string B occurs at end of string a, and print
for line in lines:
    if line:
        string, char = parse(line)
        string = string[::-1]
        searching = True
        for i in xrange(len(string)):
            if string[i] == char:
                print len(string)-1-i
                searching = False
                break

        if searching: print -1

exit(0)
