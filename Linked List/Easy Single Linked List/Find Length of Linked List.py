Find Length of Linked List

Input:
LinkedList: 1->2->3->4->5
Output: 5


Approach : We use a counter to find length and traverse the whole list. O(n),O(1)

def length(head):
	counter = 1
	curr = head
	while curr.next:
		counter+=1
		curr = curr.next
	return head