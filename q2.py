fiba = 1
fibb = 2
fibc = 0
total = 2

for i in range(1000000):
    # Calculate the next fib number
    fibc = fiba + fibb

    # Pnly working up to 4 million
    if fibc >= 4000000:
        break

    # Count the even numbers
    if fibc % 2 == 0:
        total += fibc

    # Prepare for next set of fib numbers
    fiba = fibb
    fibb = fibc

print ("Total: {}, i: {}".format(total, i))
   
