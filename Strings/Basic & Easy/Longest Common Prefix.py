Longest Common Prefix

Input: strs = ["flower","flow","flight"]
Output: "fl"


def longestcommon(strs):
	for i in range(len(strs[0])):
		for s in strs:
			if i == len(s) or s[i] != strs[0][i]:
				return res
		res+=s[i]
	return res