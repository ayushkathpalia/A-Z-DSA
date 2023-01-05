Rotate String


Input: s = "abcde", goal = "cdeab"
Output: true

Approach : If we add the input string twice, we get all posibilities of rotated strings.

O(n),O(1)

def rotateString(s,goal):
	if len(s)!=len(goal):
		return False
	tmp = s+s
	if goal in tmp:
		return True
	else:
		return False
	