Delete Node to a Doubly Linked List

# Node of a doubly linked list

class Node:
	def __init__(self, next=None, prev=None, data=None):
		
		# reference to next node in DLL
		self.next = next
		
		# reference to previous node in DLL
		self.prev = prev
		self.data = data

1.Delete Node at Beginning

Approach: Check if head is empty, check if list has only one node. We return None in both cases.We move head to next node and initialize next 
nodes prev to None and return head

O(1),O(1)

def deleteBegin(head):
	if head is None: #check if head is empty
		return None
	if head.next is None: #check if list has only one node
		return None
	head = head.next
	head.prev = None
	return head


2.Delete Last Node

Approach:Iterate to second last node and set its next to None.


def lastNode(head):
	if head is None:
		return head
	if head.next is None:
		return None
	curr = head
	while curr.next.next:
		curr = curr.next
	curr.next = None
	return head

3.Delete Node at position

LinkedList = 1 <--> 3 <--> 4 
x = 3
Output: 1 3  

def deletePos(head,pos):
	if head is None:
		return None
	if pos == 1:
		head = head.next
		head.prev = None
		return head
	counter = 1
	curr = head
	while counter < pos:
		curr = curr.next
	curr.next = curr.next.next
	curr.next.next.prev = curr
	return head