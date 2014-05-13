def sieve(n):
    sqrtn = int(n**0.5)
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, sqrtn+1):
        if sieve[i]:
            m = n//i - i
            sieve[i*i:n+1:i] = [False] * (m+1)

    sieve = [i for i in range(n+1) if sieve[i]]
    return sieve

print sieve(4294967293)

