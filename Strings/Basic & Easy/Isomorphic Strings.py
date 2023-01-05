Isomorphic Strings

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Approach: Use two dictionaries. Check if it is present in maps and values are different.else insert val in dict.

O(n),O(n)

def isomorphic(s,t):
    if len(s) != len(t):
        return False
    map1 = {}
    map2 = {}
    for i in range(len(s)):
        c1,c2 = s[i],t[i]
        if (c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2]!= c1):
            return False
        map1[c1] = c2
        map2[c2] = c1
    return True 


