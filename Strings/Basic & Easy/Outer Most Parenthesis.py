Outer Most Parenthesis

(()())(()) -> ()()()

Approach: Use stack.If opening, then check if stack > 0,append to ans . Append to stack .If closing, pop stack and append to ans 
		if stack > 0.

O(n),O(n)

def removeouter(s):
	st = []
	ans = ""
	for i in range(len(s)):
		if s[i] == '(':
			if len(st) > 0:
				ans+=s[i]
			st.append(s[i])
		else:
			st.pop()
			if len(st) > 0:
				ans+=s[i]
	return ans