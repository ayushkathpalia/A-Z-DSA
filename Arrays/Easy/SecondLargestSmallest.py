Find the Second Smallest and Second Largest Element in the array


Approach:
Second smallest: Traverse the array and check if no is smaller than smallest element , thn assign no to smallest and smallest no value 
to second smallest .
Check if no is bigger than smallest no but smaller than second smallest, then assign it to second smallest.



O(n),O(1)

def second_smallest():
	small = float('inf')
	second_small = float('inf')

	for ele in arr:
		if ele < small:
			second_small = small
			small = ele
		elif ele > small and ele < second_small:
			second_small = ele

	return second_small


def second_largest():
	large = float('-inf')
	second_large = float('-inf')

	for ele in arr:
		if ele > large:
			second_large = large
			large = ele
		elif ele < large and ele > second_large:
			second_large = ele

	return second_large