Search An Item in a Linked List

n = 4
1->2->3->4
Key = 3
Output:
True

Approach : Traverse the Linked List and check if key is present or not. O(n),O(1)

def search(head,key):
	curr = head
	while curr.next:
		if curr.val == key:
			return True
		curr = curr.next
	return False
