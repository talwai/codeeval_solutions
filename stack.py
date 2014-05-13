"""
Write a program implementing a stack inteface for integers.The interface should have 'push' and 'pop' functions. You will be asked to 'push' a series of integers and then 'pop' and print out every alternate integer.

The first argument will be a text file containing a series of space delimited integers, one per line.
"""


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

def parse(string):
    nums = [int(x) for x in string.strip().split()]
    return nums


#For each line, check if jolly jumper and print
for line in lines:
    nums = parse(line)
    ret_str = ''
    for num in nums[::-2]:
        ret_str += str(num) + ' '
    print ret_str.strip()
exit(0)
