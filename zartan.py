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


num_roads = 0
num_junctions = 0

vertices = {}
edges = []

def find_cycle(vertices, edges):
    for vertex in vertices:
        return



#For each line, find modulus and print
for i in range(0, len(lines)):
    line = lines[i].strip()
    if i == 0:
        num_junctions = int(line)
    elif i == 1:
        num_roads = int(line)
    else:
        tokens = line.split(' ')
        from_v = int(tokens[1])
        to_v = int(tokens[2])
        for x in [from_v, to_v]:
            if x not in vertices:
            	insert(x)
        edges.append((from_v, to_v))

exit(0)
