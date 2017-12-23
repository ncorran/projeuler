primes = [2,3,5,7,11,13]
n = 13
maxprime = 2000000

while primes[-1] < maxprime:
    # Check only odd numbers
    n = n + 2

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

print("Prime[{}]: {}".format(len(primes), primes[-1]))

t = 0
for i in range(len(primes) - 1):
    t = t + primes[i]

print("Total primes < {} = {}".format(maxprime, t))
