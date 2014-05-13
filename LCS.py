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

def max_len(seq_A, seq_B):
    if len(seq_A) > len(seq_B):
    	return seq_A
    else:
    	return seq_B

def LCS_len(seq_A, seq_B):
    a_len = len(seq_A)
    b_len = len(seq_B)

    lens = [[0 for x in xrange(b_len)] for x in xrange(a_len)]
    for i in xrange(a_len):
    	lens[i][0] = 0

    for j in xrange(b_len):
    	lens[0][j] = 0

    for i in xrange(a_len):
        for j in xrange(b_len):
            if seq_A[i] == seq_B[j]:
                lens[i][j] = lens[i-1][j-1] + 1
            else:
            	lens[i][j] = max(lens[i][j-1], lens[i-1][j])
    return lens

def LCS_read(lens, seq_A, seq_B, i, j):
    if i < 0 or j < 0:
    	return ""
    elif seq_A[i] == seq_B[j]:
    	return LCS_read(lens, seq_A, seq_B, i-1, j-1) + seq_A[i]
    else:
        if lens[i][j-1] > lens[i-1][j]:
        	return LCS_read(lens, seq_A, seq_B, i, j-1)
        else:
            return LCS_read(lens,seq_A, seq_B, i-1, j)

for line in lines:
    if line.strip():
        seq_A, seq_B = line.split(';')
        a_len = len(seq_A)
        b_len = len(seq_B)
        print LCS_read(LCS_len(seq_A, seq_B), seq_A, seq_B, a_len-1, b_len-1).strip()
exit(0)
