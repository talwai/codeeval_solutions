import sys

#recursive function to find modulus.
def modulus(n,m):
    try:
        n = int(n)
        m = int(m)
    except ValueError:
        print "Character cannot be parsed to int"
        return "Line contains bad character"
    if n < m:
        return n
    else: return modulus(n-m,m)

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
    vals = line.strip().split(',')
    mod = modulus(vals[0],vals[1])
    print str(mod)

exit(0)
