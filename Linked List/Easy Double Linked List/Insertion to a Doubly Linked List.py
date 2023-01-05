Insertion to a Doubly Linked List

# Node of a doubly linked list

class Node:
	def __init__(self, next=None, prev=None, data=None):
		
		# reference to next node in DLL
		self.next = next
		
		# reference to previous node in DLL
		self.prev = prev
		self.data = data



1. Insert at the Beginning 

def insertBegin(head):
    tmp = Node(x)
    if head != None:
        head.prev = tmp
    tmp.next = head
    return tmp


2.Insert at End

def InsertEnd(head):
    tmp = Node(x)
    if head is None:
        return tmp
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = tmp
    tmp.prev = curr
    return head

3.Insert At pos

def InsertPos(head,pos):
    if head is None:
	    return None
	if x == 1:
		head = head.next
		head.prev = None
		return head
    counter = 1
    curr = head
    while counter < x:
    	curr = curr.next
    	counter+=1
    if curr.next == None:
        curr.prev.next = curr.next
    else:
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    return head

