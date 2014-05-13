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
    rows, cols = int(tokens[0]), int (tokens[1])
    nums = [x for x in tokens[2].split()]
    return rows, cols, nums



def build_matrix(rows, cols, nums):
    matrix = [[0 for x in xrange(cols)] for x in xrange(rows)]
    for i in xrange(rows):
        matrix[i] = nums[i*cols:i*cols+cols]
    return matrix

def spiral(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    ret_str = ''
    if rows == 1:
    	ret_str += str(matrix[0][0])
        return ret_str

    for num in matrix[0][0:cols]:
        ret_str += str(num) + ' '

    for i in range(1, rows):
    	ret_str += str(matrix[i][cols-1]) + ' '

    for num in matrix[rows-1][-2::-1]:
    	ret_str += str(num) + ' '

    for i in range(rows-2, 0, -1):
    	ret_str += str(matrix[i][0]) + ' '

    if len(matrix[1:rows-1]) == 0:
        if len(matrix) > 2:
            return ret_str + spiral(matrix[1][1])
        else:
            return ret_str
    else:
       new_matrix = [x[1:cols-1] for x in matrix[1:rows-1]]
       return ret_str + spiral(new_matrix)

for line in lines:
    if line.strip() is not '':
        rows, cols, nums = parse(line)
        matrix = build_matrix(rows, cols, nums)
        print matrix
        print spiral(matrix).strip()
exit(0)


