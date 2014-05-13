import sys
from collections import OrderedDict
FILENAME = sys.argv[1]

#Get all substrings of string
#For any substring that occurs more than once, store length
# Return longest substring that occurs more than once

#Get all substrings
# Pointer at start, pointer at end
# Move pointer at start forward, pointer at end back, store in between string

def longest_repeated_substring(word):
    substrs = get_all_substrings(word)
    repeated = OrderedDict()
    for k, v in substrs.items():
        if len(v) > 1 and no_overlap(v):
            repeated[k] = v

    #repeated = {k:v for k,v in substrs.items() if len(v) > 1 and no_overlap(v)}
    if not repeated:
        return "NONE"
    else:
        return max(repeated.keys(), key=len)


#Assumption all indices refer to strings of same length
def no_overlap(indices):
    for i in indices:
        si, ei = i[0], i[1]
        for j in indices:
            if j is not i:
                sj,ej = j[0], j[1]
                if si <= sj <= ei:
                    return False
    return True


def get_all_substrings(word):
    start = 0
    substrs = OrderedDict()
    window = 1
    while window <= len(word):
        while start+window <= len(word):
            fin = start + window
            if not word[start:fin] in substrs:
                substrs[word[start:fin]] = [(start, fin-1)]
            else:
                substrs[word[start:fin]].append( (start, fin-1) )
            start += 1
        start = 0
        window += 1
    return substrs


class SubstringElement(object):
    def __init__(self, string, start, end):
        self.string = string
        self.start = start
        self.end = end

    def __hash__(self):
        return hash(self.string)

    def __eq__(self, other):
        return self.string == other.string

class Node(object):
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

def search(root, value):
    if not isinstance(root, Node):
        raise TypeError('Please pass in a Node object as root')
    if root.value == value:
        return root
    elif root.value < value:
        return search(root.right, value)
    elif root.value > value:
        return search(root.left, value)

if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
        for l in lines:
            l = l.replace(" ", "")
            print(longest_repeated_substring(l))
