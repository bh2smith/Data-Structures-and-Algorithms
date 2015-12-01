class Node():
	
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class Stack(Node):

	def __init__(self, value = None, next = None):
		Node.__init__(self, value)
		
	def push(self, value):
		n = Node(self.value, self.next)
		self.value = value
		self.next = n

	def peek(self):
		return self.value

	def isEmpty(self):
		return self.value == None

	def pop(self):		
		x = self.peek()
		if self.next != None:
			self.value = self.next.value
			self.next = self.next.next
		return x

class SetOfStacks():

	def __init__(self, maxheight = 10):
		self.stacks = [Stack()]
		self.maxheight = maxheight

	def push(self, new):
		if len(self.stacks[-1]) == self.maxheight:
			self.stacks.append(Stack())
		
		self.stacks[-1].push(new)

	def pop(self):
		i = 0
		m = len(self.stacks)
		while i< m and self.stacks[i].isEmpty():
			i+=1
		if i == m:
			return None
		else:
			return self.stacks[i].pop()

	def popAt(self, j):
		return self.stacks[j].pop()


class MyQueue():
	#Implements a queue using two stacks.
	def __init__(self):
		self.a = Stack()
		self.b = Stack()

	def enqueue(self, value):
		self.a.push(value)

	def dequeue(self):
		while not self.a.isEmpty():
			self.b.push(self.a.pop())
		x = self.b.pop()
		while not self.b.isEmpty():
			self.a.push(self.b.pop())
		return x

################ Utilizing Python

# class Stack():

# 	def __init__(self, top):
# 		if top == None:
# 			self.top = []
# 		else:
# 			self.top = [top]

# 	def isEmpty(self):
# 		return len(self.top) == 0

# 	def push(self, new):
# 		self.top.append(new)

# 	def pop(self):
# 		return self.top.pop()

# 	def length(self):
# 		return len(self.top)

# 	def __str__(self):
# 		return str(self.top[::-1])


# class Queue():

# 	def __init__(self, value):
# 		if value == None:
# 			self.front = []
# 		else:
# 			self.front = [value]

# 	def enqueue(self, value):
# 		self.front.insert(0,value)

# 	def dequeue(self):
# 		return self.front.pop()

# 	def __str__(self):
# 		return str(self.front)
