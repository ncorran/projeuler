val = []
arange = 100
brange = 100
for a in range(2, arange + 1):
    for b in range(2, brange + 1):
        res = a ** b
        if res not in val:
            val.append(res)

print("Distinct values: {}".format(len(val)))
