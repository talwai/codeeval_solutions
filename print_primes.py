import sys
import math

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

def sieve(divisor, lst):
    return [x for x in lst if x % divisor != 0]

def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if not n & 1:
        return False

    for x in xrange(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False

    return True

def less_primes(num):
    primes = []
    if num <= 2:
        return primes
    else:
        primes.append(2)

    to_consider = xrange(3,num,2)

    while len(to_consider) > 0:
        curr = to_consider[0]
        if is_prime(curr):
            primes.append(curr)
            to_consider = sieve(curr, to_consider)
    return primes

#For each line, find primes-less-than  and print
for line in lines:
    num = int(line)
    output_str = ''
    for i in less_primes(num):
        output_str += (str(i) + ',')
    print output_str[:-1]

exit(0)
