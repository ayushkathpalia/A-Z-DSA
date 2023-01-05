#Count Frequences of  Array 

Approach 1: Use two loops to find occcurances of each element - O(n^2)

Approach 2: Use Hashmap(Dict) to find the no of occurances

def findOcc(arr):
	hashmap = {}
	for ele in arr:
		if ele in hashmap:
			hashmap[ele]+=1
		else:
			hashmap[ele] = 1



#GET max and min Frequences

ans_max = max(hashmap, key=hashmap.get)
ans_min = min(hashmap, key=hashmap.get)