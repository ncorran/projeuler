# 2520 is the smallest number that can be divided by #s 1..10
# with 0 remainder.
# To find the smallest number divisible by 1 .. 20 evenly it must be
# a multiple of 2520
f = 2520
n = 0
success = False

# Dont let range start from 0!
for i in range(1, 100000):
    n = f*i
    success = True

    # check division by 11..20 to find the answer
    for d in range(11, 20):
        if n % d != 0:
            success = False

    if success:
        break

if success:
    print("Answer[{}]: {}".format(i, n))
else:
    print("No answer up to {} in {} checks".format(n, i))

