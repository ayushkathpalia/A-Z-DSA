Insert Node in Linked List

'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the beginning of the linked list.

    def insertAtBegining(self,head,x):
        # code here 
        new_node =Node(x)
        new_node.next = head
        return new_node

    #Insert Node at position
    def insertnodeMid(self,data,position):
        if position == 1:
            self.insertAtBegining(data)
            return
        new_node = Node(data)
        count = 1
        tmp = self.head 
        while count < position-1:
            tmp = tmp.next
            count+=1
        new_node.next = tmp.next
        tmp.next = new_node
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        if head == None:
            return Node(x)
        else:
            curr = head
            while curr.next:
                curr = curr.next
            new_node =Node(x)
            curr.next = new_node
            return head
            
