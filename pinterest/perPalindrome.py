# find palidrome in permutations of string
# 3/2/2020 Ralf Pieper 
from itertools import permutations

def isPalindrome(s):  
    return(s == s[::-1])

# true if a palidrome is found in the string
def perpal(s):
    for x in list(permutations(s)):
        i = ''.join(x)
        ispalindrome=False
        if isPalindrome(i):
            ispalindrome=True
            break

    return(ispalindrome)

# test
print(perpal("code"))
print(perpal("aab"))
print(perpal("carerac"))
