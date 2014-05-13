import sys

my_dict = {
        '0' : '0',
        '1' : '1',
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz'
       }


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

def generate_strings(phone_num):
    if len(phone_num) == 1:
    	return phone_num
    curr, rest = phone_num[0], phone_num[1:]
    all_strings = []
    for pos in my_dict[curr]:
        all_strings = all_strings + [pos+ val for val in generate_strings(rest)]

    return all_strings

#For each line, check if jolly jumper and print
for line in lines:
    phone_num = line.strip()
    ret_str = ''
    for string in sorted(generate_strings(phone_num)):
        ret_str = ret_str + str(string) + ','
    print ret_str[:-1]
exit(0)
