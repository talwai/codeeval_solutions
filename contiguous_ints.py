"""
Print to stdout, the largest sum. In other words, of all the possible contiguous subarrays for a given array, find the one with the largest sum, and print that sum.
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
    nums = [int(x) for x in string.strip().split(',')]
    return nums

#Kadane's algorithm
def max_subarray(nums):
    max_overall = max_ending_here = 0
    for num in nums:
    	max_ending_here = max(0, max_ending_here + num)
    	max_overall = max(max_ending_here, max_overall)
    return max_overall


for line in lines:
    nums = parse(line)
    print max_subarray(nums)

exit(0)


