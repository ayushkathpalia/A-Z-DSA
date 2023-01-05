Find The Missing & Repeating Number in the Array

Approach 1: Using Count

1.Take an Array of Os.
2. Iterate the original array and increment the new array acc. to the index.
3. In the new array,1 value will be 0 and other 2.
4.Index with 0 is miising no. and index with 2 is the repeating no.

 def missingno(arr):
 	n = len(arr)
 	res = [0]*n
 	for ele in arr:
 		res[ele]+=1

 	for i in range(1,len(res)):
 		if arr[i] == 0 or arr[i] == 2:
 			print(i)


Approach 2:Using Maths Linear Equation


Approach 3:Using XOR


#Leetcode & GFG:

def missingNumber(self, nums: List[int]) -> int:
    N = len(nums)
    sum1 = (N*(N+1))//2
    sum2 = 0
    for ele in nums:
        sum2+=ele
    return abs(sum1-sum2)