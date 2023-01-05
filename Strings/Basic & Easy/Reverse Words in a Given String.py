Reverse Words in a Given String

Example 1:
Input: s=”this is an amazing program”
Output: “program amazing an is this”


Approach : Split the string to a list and reverse . Then the list with " ".

def reverse(abc):
    s = abc.split()[::-1]
    res = " ".join(s)
    return res



