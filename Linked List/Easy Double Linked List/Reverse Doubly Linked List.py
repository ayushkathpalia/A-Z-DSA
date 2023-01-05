Reverse Doubly Linked List

Apporach:Iterate the list and keep swapping next & prev of the nodes.

O(n),O(1)

def reverse(head):
	if head is None:
		return None
	if head.next is None:
		return None
	curr = head
	prev = None
	while curr:
		prev = curr
		curr.next,curr.prev = curr.prev,curr.next #swap prev & next
		curr = curr.prev
	return prev
