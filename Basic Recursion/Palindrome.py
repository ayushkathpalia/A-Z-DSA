#Check if str is palindrome or not


Approach: SAme as Reverse
Algo :
1.Check if i >= n/2
2.Check if both char is not same, return False



def palindrome(s,i,n):
	if i >= n/2:
		return True
	if s[i] != s[n-i-1]:
		return False
	return palindrome(s,i+1,n)



#LEETCODE - Valid Palindrom


class Solution:
    def alphanum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        def helper(l,r):
            #base case
            if l == r:
                return True
            if l < r:
                if not self.alphanum(s[l]):
                    l+=1
                if not self.alphanum(s[r]):
                    r-=1
                if s[l].lower()!=s[r].lower():
                    return False
                helper(l+1,r-1)
            
        if len(s) == 0:
                return True
            
        l,r = 0,len(s)-1
        return helper(l,r)