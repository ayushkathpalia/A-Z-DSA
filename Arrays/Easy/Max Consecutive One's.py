Max Consecutive One -> Leetcode

nums = [1,1,0,1,1,1]

Approach : 
1.We iterate the array. 
2.Set count = 0, if we see 1, we increment the count and maxcount,
3.If we see 0, we set the count to 0

O(n),O(1)

def maxOnes(arr):
	maxcount = 0
	count = 0
	for no in arr:
		if no  == 1:
			count+=1
			maxcount = max(maxcount,count)
		else:
			count = 0

	return maxcount




#GFG
Maximize No of 1s 


