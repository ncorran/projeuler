primes = [1,2,3,5,7,11,13]
n = 13

while len(primes) < 1001:
    # Check only odd numbers
    n = n + 2

    # Check for division by primes (other than 2)
    for i in range(1, len(primes)):
        p = primes[i]
        # no prime factor of n > sqrt(n) (other than n)
        if p*p > n:
            primes.append(n)
            break

        if n % p == 0:
            # found a divisor so not prime
            break
    else:
        print("Gone wrong")
        exit()

prod = 1
mult = 1
val = []

for i in range(0, 30):
    for j in range(i, 30):
        res = primes[i] * primes[j]
        val.append(res)
    
val.sort()

print("{} divisors: {}".format(len(val), ",".join(str(v) for v in val)))


exit()

n = 1
tri = 0
maxfactors = 0

while True:
    tri = tri + n
    n = n + 1

    # what is the number of divisors
    # including 1 and itself
    # they will be multiples of primes inc. 2

    div = tri
    evens = 0
    primefactor = 0

    if div % 2 == 1:
        continue

    while div % 2 == 0:
       evens = evens + 1
       div = div >> 1
    
    for i in range(0, len(primes)):
        if primes[i] >= tri:
            break

        if tri % primes[i] == 0:
           primefactor = primefactor + 1

        f = primes[i]
        while True:
           f = f << 1
           if tri % f == 0:
               primefactor = primefactor + 1
           else:
               break

    factors = evens + primefactor + 1 #inc div by 1
    if factors > maxfactors:
        maxfactors = factors
        print("{} has {} factors ({} even, {} prime)".format(tri, factors, evens, primefactor))

    if maxfactors > 500:
        break
