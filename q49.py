primes = [2,3,5,7,11,13]
n = 13

while n < 10000:
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

i = 0
while primes[i] < 1000:
    i = i + 1

primes = primes[i:]
    
#print("4 digit primes[{}]: {}".format(len(primes), ",".join(str(p) for p in primes)))

def permutes(s1, s2):
    for c in list(s1):
        if c not in s2:
            return False
    for c in list(s2):
        if c not in s1:
            return False
    return True

for p1 in primes:
    # inc by steps of 18 to keep diff as multiple of 18
    # starting high enough to change the first digit of
    # the solution
    for i in range(486, 5000, 18):
        p2 = p1+i
        p3 = p2+i
        if p2 in primes and p3 in primes:
            sp1 = str(p1)
            sp2 = str(p2)
            sp3 = str(p3)
            if permutes(sp1, sp2) and permutes(sp1, sp3):
                print("3 primes {},{},{} with common diff of {}".format(p1, p2, p3, i))

