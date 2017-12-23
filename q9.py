squares = []
n = 1000

# Set up a list of squares to check against
for i in range(1, n):
    squares.append(i*i)

# Check all a^2 + b^2 = c^2 for sum a+b+c = n
# Then find a*b*c
for a in range(1, n):
    # a < b < c, so start b from a+1
    for b in range(a+1, n):
        csq = a*a + b*b
        # only check the cases where the sum is a square
        if csq in squares:
            c = squares.index(csq) + 1
            sumabc = a+b+c
            #print("Candidate: {} from {}^2 + {}^2 = {}^2. Sum {}".format(csq, a, b, c, sumabc, a*b*c))
            if sumabc == n:
                print("Result: {}^2 + {}^2 = {}^2. Sum {}. Prod {}".format(a, b, c, sumabc, a*b*c))
                exit()
