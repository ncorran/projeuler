# Sum the squares
# Sum the numbers and square
# Find the difference

terms = 100

def sum_of_squares (n):
    sumsq = 0
    for x in range(1, n+1):
        sumsq = sumsq + x*x
    return sumsq

def square_of_sum (n):
    sumn = 0
    if n % 2 == 0:  
        sumn = (1 + n) * (int)(n/2)
    else:
        sumn = n * (int)(n/2)

    return sumn * sumn

sqsum = square_of_sum(terms)
sumsq = sum_of_squares(terms)
   
print("Answer[{}]: sqsum:{}, sumsq:{}, diff:{}".format(terms, sqsum, sumsq, sqsum-sumsq))
