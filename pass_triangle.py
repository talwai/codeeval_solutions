import sys
import pdb


#Data structure to hold individual nodes, with pointers to left subtree and right subtree
class node:
    def __init__(self,val,left=None, right=None,score = -1):
        self.val = val #Value of node
        self.left = left #Left node
        self.right = right #Right node
        self.score=score #Current max sum of node + its best subtree. -1 indicates node is still unscored

#Check for correct number of arguments
if len(sys.argv) is not 2:
    sys.exit('Wrong Argument Length. Usage: python pass_triangle.py [filename]')

filename = sys.argv[1]

#Open file and read in lines, exit if file does not exist
try:
    with open(filename) as f:
        raw_lines = f.readlines()
except IOError:
    exit('File ' + filename + ' does not exist')

#Dictionary to hold lines processed from text file
lines = {}

#Dictionary to indicate nodes that have been visited in DFS
nodes = {}

#Read in numbers from raw lines, place them in 2D array lines
#Populate nodes with all Nones to indicate that all nodes are yet unvisited
for i in range (0,len(raw_lines)):
    nums = raw_lines[i].strip().split(' ')
    lines[i] = [(num, False) for num in nums] #Read in each number as tuple (num, False) since number has not yet been visited in DFS
    nodes[i] = [ None for j in range (0,len(lines[i])) ]

#Utility function to look up node in nodes dictionary, based on:
#Cursor: Line number, and root_index: position of number in line
def lookup_node (cursor, root_index):
    if lines[cursor][root_index][1] == True:
        return nodes[cursor][root_index]
    else:
        return None

#Add visited node to dictionary, mark number as True in lines array
def add_node (node, cursor, root_index):
    lines[cursor][root_index] = (lines[cursor][root_index][0],True)
    nodes[cursor][root_index] = node


#Recursive DFS to create nodes from lines
def search(root_index, cursor):
    n = lookup_node (cursor, root_index)

    #If node is unvisited
    if n == None:
        if cursor == (len(lines) -1):
            n = node(lines[cursor][root_index][0])
        elif len(lines[cursor+1]) < (root_index + 2):
            if len(lines[cursor+1]) < (root_index + 1):
                n = node(lines[cursor][root_index][0])
            else: n = node (lines[cursor][root_index][0],left=search(root_index,cursor+1)) #Get left subtree
        else:
            n = node (lines[cursor][root_index][0], left=search(root_index,cursor+1),right=search(root_index+1,cursor+1)) #Get left+right subtrees
        add_node(n,cursor,root_index)

    return n


#Recursively compute maximum-sum path along tree
def sum_tree(node):
    #Score node based on maximum sum of its subtrees
    if node.left == None and node.right == None:
        node.score = int(node.val)
    elif node.right == None:
        if node.left.score == -1: #if left node still unscored
            node.score = (int(node.val) + sum_tree(node.left))
        else:
            node.score = (int(node.val) + node.left.score)
    else: #if right and left nodes still unscored
        if node.left.score == -1 and node.right.score == -1:
            node.score = (int(node.val) + max(sum_tree(node.left),sum_tree(node.right)) )
        elif node.left.score == -1:
            node.score = (int(node.val) + max(sum_tree(node.left),node.right.score))
        elif node.right.score == -1:
            node.score = (int(node.val) + max(node.left.score,sum_tree(node.right)) )
        else:
            node.score = (int(node.val) + max(node.left.score,node.right.score))

    #Return score i.e. max sum of node + subtree
    return node.score

#DFS of tree from root i.e. lines[0][0]
tree = search (0,0)

#Get max sum along tree and print it
print sum_tree(tree)

exit(0)

