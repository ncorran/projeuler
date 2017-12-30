def pentagon(n):
    return int(n*(3*n - 1) / 2)

# find pair of pentagonal numbers where
# - sum and difference are pentagonal numbers
# - then find minimal difference of such pairs

# We want to check as we go whether we have a solution
# and the first solution will be the minimal answer

# Assume the pentagon number we are looking at is the sum
# - i.e. largest pentagon number we need
# - the sum is Pi + Pj
# - check if any existing Pj in the set of numbers
#   has a Pi (= s - Pj) that is a member
# - also check the diff is present (= s - Pj - Pj)
pent = set()
n = 0
while True:
    n = n + 1
    ps = pentagon(n)
    for pj in pent:
        if ps - pj in pent and ps - pj - pj in pent:
            print("Minimal diff = {} from {},{}".format(ps - pj - pj, pj, ps - pj))
            exit()
    else:
        # no match - add to set and continue
        pent.add(ps)
