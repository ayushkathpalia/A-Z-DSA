Check if array is Sorted


[1,2,3,4,5]

 
Approach:
In a sorted array, elements are increasing as we go right. CHeck if the element is smaller or equal to the right element.

O(n),O(1)
def isSorted(arr):
    if n == 1:
            return True
	for j in range(1,len(arr)):
		if arr[j] < arr[j-1]:
			return False
	return True



#LeetCode:

Check if the array is sorted and Rotated.

Input: nums = [3,4,5,1,2]
Output: true

Input: nums = [2,1,3,4]
Output: false

Approach:
take a variable 'count'. Check if the array is sorted, if not  increment count. 
check if first ele is smaller than last ele in arr, if yes increment count
check if count <= 1.return True else false


If arr is sorted but not rotated then we return false, as it is rotated 0 times. -> [1,2,3,4,5]

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1,len(nums)):    
            if nums[i-1] > nums[i]:           #True for 1.sorted and roated , 2.only rotated
                count+=1

        if nums[0] < nums[len(nums)-1]:			#True for 1.only sorted, 2.only rotated
            count+=1
        
        if count<=1:
            return True
        else:
            return False


