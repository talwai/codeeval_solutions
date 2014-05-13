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


def is_palindrome(num):
    return str(num)[::-1] == str(num)


def reverse_digits(num):
    return int(str(num)[::-1])

# For each line find palindrome and print

for line in lines:
    count = 0
    num = int(line.strip())
    while not is_palindrome(num): #loop until sum is palindrome
        num += reverse_digits(num)
        count += 1
    print str(count) + ' ' + str(num)

exit(0)
