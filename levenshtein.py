import sys

class LevenshteinGraph(object):
    def __init__(self, words):
        self.vertices = [LevenshteinVertex(word) for word in words]
        self.generate_edges()

    def generate_edges(self):
        for v in self.vertices:
            v.adj = [vx for vx in self.vertices if is_sibling(v.word, vx.word) and v is not vx]

    def find_vertex_by_word(self, word):
        for v in self.vertices:
            if v.word == word:
                return v

    def immediate_siblings(self, word):
        v = self.find_vertex_by_word(word)
        return [vx.word for vx in v.adj]

    def query(self, v, acc=None):
        v = v if isinstance(v, LevenshteinVertex) else self.find_vertex_by_word(v)
        acc = acc if acc is not None else [v.word]
        for vert in v.adj:
            if vert.word not in acc:
                acc.append(vert.word)
                self.query(vert, acc)
        return len(acc)


class LevenshteinVertex(object):
    def __init__(self, word):
        self.word = word
        self.adj = []


def is_sibling(a,b):
    both = [a,b]
    len_diff = abs(len(a)-len(b))

    # Length difference greater than 1 => Not friends
    if len_diff > 1:
        return False
    elif len_diff == 1:
        #Every character in shorter must appear in longer, in SAME ORDER
        both = sorted(both, key=lambda x: len(x))
        shorter, longer = both[0], both[1]

        i = 0
        offset = 0

        while i < len(shorter):
            if shorter[i] != longer[i+offset]:
                offset += 1
            else:
                i += 1

            #Indicates word distance > 1, not friends
            if offset > 1:
                return False
    elif len_diff == 0:
        #Minimum 1 character difference between a and b
        dist = 0
        for i in range(0, len(a)):
            if a[i] != b[i]:
                dist += 1
        if dist > 1:
            return False

    return True

if __name__ == '__main__':
    with open('lev_test.txt') as f:
        lines = f.readlines()
        words = [line.strip() for line in lines]

    graph = LevenshteinGraph(words)
    #graph.query('apple')
