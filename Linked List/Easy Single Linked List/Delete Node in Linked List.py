Delete Node in Linked List


1.Delete Last Node in LL.

Approach : Iterate to the second last node. by checking if head.next.next is null. Then assign None to head.next
O(n),O(1)

def deleteLastNode(head):
	curr = head
	while curr.next.next:
		curr = curr.next
	curr.next = None


2.Delete node X from the Linked List (LeetCode) (only node was given)

Approach : Seting its val to next node val and its next to next node's next. O(1),O(1)

def deleteNodeX(head,x):
    node.val = node.next.val
    node.next = node.next.next


3.Delete Node from a Position from the Linked List.

Approach :If pos == 1 , the we just change the head to head.next.Else we use prev to store the prev node and curr to store the current node and we use counter to get position of the node.we change prev.next to curr.next to delete the curr node acc to the pos given. O(n),O(1)

def deleteNode(head,pos):
    if position == 1:
        tmp = head
        head = head.next
        del tmp
    else:
        curr = head
        prev = None
    
        counter = 1
        while counter < position:
            prev = curr
            curr = curr.next
            counter+=1
        
        prev.next = curr.next
        curr.next = None
        del curr
    return head
