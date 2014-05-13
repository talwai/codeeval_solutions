cache = {}

def get_adj(pos):
    adj = []
    if pos[0] is 1:
    	adj.append([pos[0] + 1, pos[1] ])
        if pos[1] in [2, 3]:
            adj.append([pos[0], pos[1]+1])
            adj.append([pos[0], pos[1]-1])
        elif pos[1] is 1:
            adj.append([pos[0], pos[1]+1])
        else: adj.append([pos[0], pos[1]-1])

    elif pos[0] in [2,3]:
        adj.append([pos[0]-1, pos[1]])
    	adj.append([pos[0]+1, pos[1]])
        if pos[1] in [2, 3]:
            adj.append([pos[0], pos[1]+1])
            adj.append([pos[0], pos[1]-1])
        elif pos[1] is 1:
            adj.append([pos[0],pos[1]+1])
        else: adj.append([pos[0],pos[1]-1])
    else:
    	adj.append([pos[0]-1,pos[1]])
        if pos[1] in [2,3]:
            adj.append([pos[0],pos[1]+1])
            adj.append([pos[0],pos[1]-1])
        elif pos[1] is 1:
            adj.append([pos[0],pos[1]+1])
        else: adj.append([pos[0],pos[1]-1])
    return adj



def get_adj_2(pos):
    if pos == [1,1]:
    	return [[1,2],[2,1]]
    elif pos == [1,2]:
    	return [[1,1],[2,2]]
    elif pos == [2,1]:
    	return [[1,1],[2,2]]
    else:
    	return [[1,2],[2,1]]

path = []
count = 0
GLOBAL_FINISH = [4,4]

def moves_between(start, finish):
    global path, count

    if start == finish:
    	return 1

    ll = [start, finish]
    flat = [item for sublist in ll for item in sublist]
    #print ll


    if tuple(flat) in cache:
    	return cache.get(tuple (flat))

    if start not in path or not path:
        path.append(start)



    #print "Get adj ", get_adj_2(start)

    adj_trim = [adj for adj in get_adj(start) if adj not in path]

    if GLOBAL_FINISH in adj_trim:
            if len(adj_trim) == 1:
            	return 1
            else:
                total = reduce(lambda x, y: x * y, [moves_between(adj, GLOBAL_FINISH) for adj in adj_trim],1 ) +1

                cache[ tuple(flat) ] = total
      #          print " Global returning ", total
                count += total
                if len(path) > 0 and start in path:
         	        path = path[:path.index(start)+1]
                return total

    if finish in adj_trim:
        if len(adj_trim) is 1:
       # 	print " returning 1"
        	return 1
        else:
            total = reduce(lambda x, y: x * y, [moves_between(adj, finish) for adj in adj_trim],1 ) + 1


            cache[ tuple(flat) ] = total
        #    print " returning ", total

            if len(path) > 0 and start in path:
        	    path = path[:path.index(start)+1]

            return total

    elif not adj_trim:
        return 1;

    else:
    	l = [moves_between(start,adj) * moves_between(adj, finish) for adj in adj_trim]
        total = sum(l)
        cache[ tuple(flat) ] = total

        if len(path) > 0 and start in path:
             path = path[:path.index(start)]

        return total


moves_between([1, 1], [4, 4])
print count
exit(0)




