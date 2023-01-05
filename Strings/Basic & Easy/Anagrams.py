Anagrams

Input: s = "anagram", t = "nagaram"
Output: true

Approach 1: Sort both Strings and check if they are equal. 
	O(nlogn) , O(1)

def anagram(s1,s2):
	if len(s1)!=len(s2):
		return False
	s1 = sorted(s)
	s2 = sorted(t)
	if s1 == s2:
	    return True
	else:
	    return False

Approach 2:Iterate the first str , store the frequencey of all aplhabets. Iterate second str and decrease the frequency in the same dict. If all zero, then return True else False.

	O(n),O(len(str))

def anagram(s1,s2):
	if len(s1)!=len(s2):
		return False
	help = {}
	for i in range(len(s1)):
		if s1[i] in help:
			help[s1[i]]+=1
		else:
			help[s1[i]] =1
	for i in range(len(s2)):
		if s1[i] in help:
			help[s1[i]]-=1

	if help:
		return False
	else:
		return True

		OR

def anagram(a,b):
    if len(a) != len(b):
        return False
        
    char = [0]*256
    
    for i in range(len(a)):
        char[ord(a[i])] += 1
        char[ord(b[i])] -= 1

    for x in char:
        if x != 0:
            return False
        
    return True




	

