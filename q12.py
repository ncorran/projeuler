n = 1
tri = 0

while True:
    tri = tri + n
    n = n + 1

    # what is the number of divisors
    # including 1 and itself
    # they will be multiples of primes
    print("{}".format(tri))
