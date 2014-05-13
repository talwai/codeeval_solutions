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
def getPerms(string):
    if len(string) == 1:
    	return string
    perms = []
    for i in xrange(len(string)):
        char = string[i]
        for perm in getPerms(string[0:i] + string[i+1:]):
            perms.append(char + perm)
    return perms

for line in lines:
    ret_str = ''
    string = line.strip()
    for perm in sorted(getPerms(string)):
        ret_str = ret_str + perm + ','
    print ret_str[:-1]
exit(0)
