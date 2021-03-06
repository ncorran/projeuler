primes = [2,3,5,7,11,13]
n = 13

while len(primes) < 10001:
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

print("Prime[{}]: {}".format(len(primes), primes[10000]))
