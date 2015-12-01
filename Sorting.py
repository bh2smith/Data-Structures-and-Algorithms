# Sorting out sorting!

def swap(A,i,j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp


# QUICKSORT (in place)

def partition(A,s,e):
	piv = A[e]
	for i in range(s,e-1):
		if A[i] < piv:
			swap(A,s,i)
			s+=1
	swap(A,s,e)
	return s

def quickSort(A,s,e):
	if s<e:
		p = partition(A,s,e)
		quickSort(A,s,p)
		quickSort(A,p+1,e)

# INSERTIONSORT (in place)
def insertionSort(A):    
    for i in range(1,len(A)):        
        v = A[i]
        j = i-1
        while j >= 0 and A[j]>v:            
            A[j+1] = A[j]
            j-=1
        A[j+1] = v   

    return A #Not all that necessary


# MERGESORT (NOT in place)

def merge(L,R):
	M = []
	i, j = 0,0
	for k in range(len(L) + len(R)):
		if (i<len(L) and j<len(R) and L[i]<=R[j]) or (i<len(L) and j == len(R)):
			M.append(L[i])
			i += 1
		else:
			M.append(R[j])
			j += 1
	return M

def mergeSort(A):
	if len(A) <= 1:
		return A
	m = len(A)/2
	L = mergeSort(A[:m])
	R = mergeSort(A[m:])
	M = merge(L, R)
	return M

# HEAPSORT

class MinHeap():

    def __init__(self):
        self.h = []

    def peek(self):
        if self.h ==[]:
            return None
        else:
            return self.h[0]

    def insert(self,value):
        self.h.append(value)
        at = len(self.h) - 1
        parent = (at-1)/2
        while at != 0 and self.h[parent]>self.h[at]:
            self.swap(at,parent)
            at = parent
            parent = (at-1)/2
    
    def popRoot(self):
        self.swap(0,-1)
        ret = self.h.pop()
        at = 0
        while self.hasChild(at) and self.h[at]>self.h[self.minChildIndex(at)]:
            k = self.minChildIndex(at)
            self.swap(at,k)
            at = k
        return ret
    
    def isEmpty(self):
        return self.h == []

    # Helper Methods
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

def heapSort(A):
	mA = MinHeap()
	for a in A:
		mA.insert(a)
	for i in range(len(A)):
		A[i] = mA.popRoot()
