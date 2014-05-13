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



def sum_of_square_digits(num):
    num = str(num)
    sum = 0
    for char in num:
        sum += int(char)**2
    return sum

#For each line, find modulus and print
for line in lines:
    s = int(line.strip())
    visited = []
    happy_flag = 1

    while s != 1:
        s = sum_of_square_digits(s)
        if s in visited:
            happy_flag = 0
            break
        visited.append(s)

    print happy_flag

exit(0)
