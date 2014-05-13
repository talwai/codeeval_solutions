import sys

def fibonacci(num):
    if num <= 1:
        return num
    else: return fibonacci(num - 1) + fibonacci(num - 2)

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print ( fibonacci(int(line)) )

