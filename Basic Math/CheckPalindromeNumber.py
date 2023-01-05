#Check Palindrome Number

def palindrome(n):
	ans = 0
	tmp = n
	while tmp:
		rem = tmp %10
		ans = ans *10 + rem
		tmp = tmp//10

	if ans == n:
		return True
	else:
		return False

#LeetCode -> Palindrome Number

def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    ans = 0
    tmp = x
    while tmp:
        rem = tmp %10
        ans = ans *10 + rem
        tmp = tmp//10

    if ans == x:
        return True
    else:
        return False
 