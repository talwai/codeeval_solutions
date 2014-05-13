"""
You are given a sorted array of positive integers and a number 'X'. Print out all pairs of numbers whose sum is equal to X. Print out only unique pairs and the pairs should be in ascending order
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
    tokens = string.strip().split(';')
    total_sum = int(tokens[1])
    nums = [int(x) for x in tokens[0].split(',')]
    return nums, total_sum

#For each line, check if jolly jumper and print
for line in lines:
    nums, total_sum = parse(line)
    nums = sorted(nums)
    pairs = []
    for i in xrange(len(nums)):
        num, rest = nums[i], nums[i+1:]
        if total_sum - num in rest:
            if (num, total_sum - num) not in pairs:
                pairs.append((num,total_sum - num))
    ret_str = ''
    if not pairs:
    	print 'NULL'
    else:
    for pair in pairs:
    	ret_str = ret_str + str(pair[0])+ ',' + str(pair[1]) + ';'
    print ret_str[:-1]

exit(0)
