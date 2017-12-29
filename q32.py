digits = ["1","2","3","4","5","6","7","8","9"]

# find all 1,2,3 and 4 digit combinations

vals1 = []
vals2 = []
vals3 = []
vals4 = []

for i in range(0, len(digits)):
    vals1.append(digits[i])

for i in range(0, len(digits)):
    for j in range(0, len(digits)):
        if i != j:
            vals2.append(digits[i]+digits[j])

for i in range(0, len(digits)):
    for j in range(0, len(digits)):
        for k in range(0, len(digits)):
            if i != j and i != k and j != k:
                vals3.append(digits[i]+digits[j]+digits[k])

for i in range(0, len(digits)):
    for j in range(0, len(digits)):
        for k in range(0, len(digits)):
            for l in range(0, len(digits)):
                if i != j and i != k and i != l and j != k and j !=l and k != l:
                    vals4.append(digits[i]+digits[j]+digits[k]+digits[l])

#print("{}".format(",".join(str(v) for v in valsx)))

def uniqdigital(s1, s2):
    for i in range(0, len(s1)):
        if s1[i] in s2:
            return False
    return True

def search(valsa, valsb):
    for i in range(0, len(valsa)):
        for j in range(0, len(valsb)):
            comb = valsa[i] + valsb[j]
            prod = str(int(valsa[i]) * int(valsb[j]))

            if len(comb) == 5 and len(prod) == 4 and not "0" in prod and len(set(list(prod))) == len(prod):
                if uniqdigital(valsa[i], valsb[j]) and uniqdigital(prod, valsa[i]+valsb[j]):
                    #print("Option of {} x {} = {} has dup digits".format(valsa[i], valsb[j], prod))
                    if prod not in res:
                        res.append(prod)
                        print("Option of {} x {} = {}".format(valsa[i], valsb[j], prod))



# find any multiple of these numbers that uses the remaining digits from 1..9
#  total digits will be 9 so the prod must be a 1 digit x a 4 digit
#  or a 2 digit x a 3 digit number
res = []
search(vals1, vals4)
search(vals2, vals3)

print("{} solutions, sum: {}".format(len(res), sum(int(i) for i in res)))
