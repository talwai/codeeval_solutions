import sys

hex_map = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
}

def compute_dec(num):
    result = 0
    for i in range(0, len(num) ):
        try:
            result += hex_map[num[i]]* (16** (len(num) - i - 1) )
        except KeyError:
            print 'Bad Input'
            return '-1'
    return result


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

#For each line, add digits and print sum
for line in lines:
    num = line.strip()
    result = compute_dec(num)
    if result != '-1':
         print result

exit(0)
