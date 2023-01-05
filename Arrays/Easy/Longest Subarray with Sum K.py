Longest Subarray with Sum K -> GFG

Approach 1: Use 2 loops to find the sum and length -> O(n^2),O(1)


def subarray(arr):
	maxlength = 0
	for i in range(len(arr)):
		sum = 0
		for j in range(i,len(arr)):
			sum += arr[j]
			if sum == k:
				maxlength = max(maxlength,(j-i+1))

	return maxlength


Approach 2: Sliding Window Technique - O(n)
1.We add the elements in the array.If the sum is smaller than target, we keep adding.
when it exceeds the limit , we shrink the window by incrementing the starting position.

This technique doesnt not work with negative elements.

def subarray(arr):
    i, j, sum = 0, 0, 0
    maxLen = 0
   
    while (j < N):
        sum += A[j]
        if (sum < K):
            j += 1
        elif (sum == K):
            maxLen = max(maxLen, j - i + 1)
            j += 1
        elif (sum > K):
            while (sum > K):
                sum -= A[i]
                i += 1
            if (sum == K):
                  maxLen = max(maxLen, j - i + 1)
            j += 1
    return maxLen

Approach 3:Prefix Sum , Using HashMap to store the max length
We keep adding sum , when sum > k then we check if sum-k is present in the dict , then we find the max length i-d[sum-k] else we store the sum in d.

def subarray(arr):
	d = {}
	sum = 0
	maxLen = 0
	for i in range(n):
		sum+=arr[i]
		if sum == k:
			maxLen = i + 1
		elif (sum-k) in d:
			maxLen = max(maxLen,i-d[sum-k])
		if sum not in d:
			d[sum] = i

	return maxLen


