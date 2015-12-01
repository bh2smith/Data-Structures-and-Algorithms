####################
#Max and Min heaps

class MaxHeap():

	def __init__(self):
		self.h = []

	def peek(self):
		if self.h ==[]:
			return None
		else:
			return self.h[0]

	def size(self):
		return len(self.h)

	def insert(self,value):
		self.h.append(value)
		at = len(self.h) - 1
		parent = (at-1)/2
		while at != 0 and self.h[parent]<self.h[at]:
			self.swap(at,parent)
			at = parent
			parent = (at-1)/2

	def hasChild(self,i):
		if 2*i+2 <= len(self.h):
			return True
		return False

	def maxChildIndex(self, i):
		if 2*i + 2 >= len(self.h) or self.h[2*i+1]>self.h[2*i+2]:
			return 2*i + 1
		else:
			return 2*i + 2

	def swap(self,i,j):
		temp = self.h[i]
		self.h[i] = self.h[j]
		self.h[j] = temp

	def popRoot(self):
		self.swap(0,-1)
		ret = self.h.pop()
		at = 0
		while self.hasChild(at) and self.h[at]<self.h[self.maxChildIndex(at)]:
			k = self.maxChildIndex(at)
			self.swap(at,k)
			at = k
		return ret

	def __str__(self):
		return str(self.h)

class MinHeap():

	def __init__(self):
		self.h = []

	def peek(self):
		if self.h ==[]:
			return None
		else:
			return self.h[0]

	def size(self):
		return len(self.h)

	def insert(self,value):
		self.h.append(value)
		at = len(self.h) - 1
		parent = (at-1)/2
		while at != 0 and self.h[parent]>self.h[at]:
			self.swap(at,	parent)
			at = parent
			parent = (at-1)/2

	def isEmpty(self):
		return self.h == None

	def hasChild(self,i):
		if 2*i+2 <= len(self.h):
			return True
		return False

	def minChildIndex(self, i):
		if 2*i + 2 >= len(self.h) or self.h[2*i+1]<self.h[2*i+2]:
			return 2*i + 1
		else:
			return 2*i + 2

	def swap(self,i,j):
		temp = self.h[i]
		self.h[i] = self.h[j]
		self.h[j] = temp

	def popRoot(self):
		self.swap(0,-1)
		ret = self.h.pop()
		at = 0
		while self.hasChild(at) and self.h[at]>self.h[self.minChildIndex(at)]:
			k = self.minChildIndex(at)
			self.swap(at,k)
			at = k
		return ret

	def __str__(self):
		return str(self.h)

# #APPLICATION 1 - Running Medians
# #APPLICATION 2 - Minimum average waiting time
