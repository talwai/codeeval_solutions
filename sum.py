import sys

#Function to add together digits of a single number, and return sum total
def add_digits(num):
    sum_total = 0
    for digit in num:
        try:
            digit = int(digit)
        except ValueError:
            print digit + ' is not an integer'
            return 'Number contains bad character'
        sum_total = sum_total + digit
    return sum_total

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
    sum_total = 0
    num = line.strip()
    sum_total = add_digits(num)
    print str(sum_total)

exit(0)
