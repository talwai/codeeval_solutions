import sys

class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

leaf_A = Node(10)
leaf_B = Node(29)
leaf_C = Node(3)
leaf_D = Node(52)

tree_A = Node(20, leaf_B, leaf_A)
tree_B = Node(8, tree_A, leaf_C)
tree_main = Node(30, leaf_D, tree_B)


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


def parse(line):
    a1, a2 = [int(x) for x in line.strip().split()]
    return a1, a2


def search(root, value, path = []):
    if root.value == value:
    	return path
    elif root.value > value:
        path.append(root.value)
        return search(root.right, value, path)
    else:
    	path.append(root.value)
    	return search(root.left, value, path)

def LCA(a1, a2):
    path_1 = search(tree_main, a1, [])
    path_2 = search(tree_main, a2, [])
    lca = None
    for i in xrange (min(len(path_1), len(path_2))):
        if path_1[i] == path_2[i]:
        	lca = path_1[i]
    return lca

for line in lines:
    a1, a2 = parse(line)
    print LCA(a1, a2)
exit(0)
