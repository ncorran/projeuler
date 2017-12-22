f1 = 1000
f2 = 1000

def palindrome(n):
    # Convert n to string
    # Make sure it is of even length (as we are comparing the two halves)
    # Split in half and reverse the second half 
    # Check for equality
    s = str(n)
    l = len(s)
    if l % 2 == 0:
        l = (int) (l / 2)
        s1 = s[0:l]
        s2 = "".join(reversed(s[-l:]))
        #print ("{}, {}".format(s1,s2))
        if s1 == s2:
            return True
    return False

print("Palindrome check for: 123321 returns {}".format(palindrome(123321)))
print("Palindrome check for: 123123 returns {}".format(palindrome(123123)))

# Assume the answer is two factors somewhere in the 900s
for i in range(100):
    # By setting f2 to f1 in this outer loop we avoid x,y and y,x answers
    f2 = f1
    f1 = f1 - 1
    for j in range(f2-900):
        f2 = f2 - 1
        # Counting down from the top should find the largest palindrome first
        guess = f1 * f2
        if palindrome(guess):
            print("Palindrome: {}, factors {}, {}".format(guess, f1, f2))
            break

