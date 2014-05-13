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
    present = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s = line.strip().replace(' ','').lower()
    for char in s:
        if char in present:
            present.remove(char)

    if len(present) == 0:
        print 'NULL'

    else:
        for char in present:
            sys.stdout.write(char)

        sys.stdout.write('\n')

exit(0)
