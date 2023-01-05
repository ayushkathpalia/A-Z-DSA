Implementing Queue Using Array

Approach Using rear and front pointers. Rear points to the last index of the array .Front points to the first index of the array that can be popped out.

Enque
Deque


class Queue:
	def __init__(self,cap):
		self.cap = cap
		self.arr = [None]*cap
		self.size = 0
		self.front = 0

	def getFront(self):
		if self.isEmpty():
			return -1
		else:
			return self.front

	def getRear(self):
		if self.isEmpty():
			return -1
		else:
			return(self.front+self.size-1)%self.cap

	def enque(self,x):
		if self.isFull():
			return None
		rear = self.getRear()
		rear = (rear+1) % self.cap
		self.arr[rear] = x
		self.size+=1

	def deque(self):
		if self.isEmpty():
			return None
		res = self.arr[self.front]
		self.front = (self.front+1)%self.cap
		self.size-=1
		return res

	def isFull(self):
		return self.size == self.cap

	def isEmpty(self):
		return self.size == 0i

Implemening Queue Using List:

class MyQueue:    
    def __init__(self):
        self.arr = []
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if len(self.arr) == 0:
            return -1
        res = self.arr.pop(0)
        return res
         # add code here


