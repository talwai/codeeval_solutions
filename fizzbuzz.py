import sys

def is_divisible(a,b,num):

    try:
        remainder_a = num % a
        remainder_b = num % b
    except ZeroDivisionError:
        print 'Division by zero not possible'
        return '-1'

    ret_str = check_remainder_a(remainder_a) + check_remainder_b(remainder_b)

    if ret_str is '':
        return num
    else: return ret_str

def check_remainder_a(num):
    if num == 0:
        return 'F'
    else: return ''

def check_remainder_b(num):
    if num == 0:
        return 'B'
    else: return ''

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
    vals = line.strip().split(' ')
    try:
        limit = int(vals[2])
        divisor_a = int(vals[0])
        divisor_b = int(vals[1])
    except ValueError:
        print 'Bad input'
        break

    for i in range (1,limit+1):
        to_print = is_divisible(divisor_a,divisor_b,i)
        if to_print == '-1':
            break
        sys.stdout.write(str(to_print) + ' ')
    print ('\r')
exit(0)
