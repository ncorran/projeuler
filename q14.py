def collatz(i):
    n = i
    terms = 0
    while n != 1:
        terms = terms + 1
        if n % 2 == 0:
            #even
            n = n >> 1 
        else:
            n = 3*n + 1
        #if terms % 1000:
            #print("Working on {}, term {}, val {}".format(i, terms, n)) 

    return terms

besti = 0
maxterms = 0
# Assume longest chain is in the top 25% of starting numbers
# and odd (as that immediately makes the sequence start higher
for i in range(999999, 750001, -2):
    terms = collatz(i)
    if terms > maxterms:
        maxterms = terms
        besti    = i
        print("Current best: {} has {} terms".format(besti, maxterms))

