Implementing Stack Using Array

Stack has 5 operations:
Push
Pop
Top
Size
isEmpty


Approach: Using Top Pointer which points to the top of the array.

class Stack:
	def __init__(self,size):
		self.arr = [-1]*size
		self.top = -1

	def push(self,x):
		self.top +=1
		self.arr[self.top] = x

	def pop(self):
		if self.top == -1:
            return -1
		self.arr[self.top] = None
		self.top-=1

	def top(self):
		return self.arr[self.top]

	def isEmpty(self):
		if self.top == -1:
			return True
		else:
			return False

	def size(self):
		return self.top+=1


Approach : Using Python List

class Stack:
	def __init__(self):
		self.arr = []

	def push(self,x):
		self.arr.append(x)

	def pop(self):
		if len(self.arr) == 0:
            return -1
		self.arr.pop()

	def top(self):
		return self.arr[-1]

	def isEmpty(self):
		if len(self.arr) == 0:
			return True
		else:
			return False

	def size(self):
		return len(self.arr)