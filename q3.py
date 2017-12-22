n = 600851475143

def factorise(n): 
    d = 2
    fact = []

    # Limut the loop, just in case of logic errors
    for i in range(1000000):
        # Check if (an incrementing) d is a factor
        # If it is store it in the list of factors, divide n and carry on
        r = n % d
        if r == 0:
            fact.append(d)
            n = n / d
        d = d + 1

    return fact

fact = factorise(n)
factors = " ".join(str(f) for f in factorise(n))
print ("{} has the following factors: {}".format(n, factors))
