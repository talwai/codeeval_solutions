def egg_drop(n,k):
    if k == 1 or k == 0:
    	return k
    if n == 1:
        return k

    return min( max(egg_drop(n-1,x-1),egg_drop(n,k-x)) for x in range(1,k+1) )

print egg_drop(2,4)
