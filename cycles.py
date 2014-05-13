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
def detect_cycles(line):
    nums = [int(x) for x in line.split(' ')]
    present = []
    for i in xrange(len(nums)):
        num = nums[i]
        if num in present:
            return nums[nums.index(num):i]
    	present.append(num)
    return []

for line in lines:
    ret_str = ''
    for num in detect_cycles(line):
        ret_str = ret_str + str(num) + ' '
    print ret_str.strip()
exit(0)
