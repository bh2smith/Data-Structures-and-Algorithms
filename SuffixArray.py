# This is usually O(N^2log(N)), as shown here
def get_suffix_array(str): 
     return sorted(range(len(str)), key=lambda i: str[i:]) 

# but can be made O(Nlog^2(N))
# THIS IS NOT WORKING.
class myTuple():
	def __init__(self,o,f=0,h=0):
		self.originalindex = o
		self.firsthalf = f
		self.secondhalf = s
	def __str__(self):
		return str(self.originalindex)+ ','+  str(self.firsthalf)+ ','+ str(self.secondhalf)

def compare(a,b):
	if a.firsthalf == b.firsthalf:
		return a.secondhalf - b.secondhalf
	return a.firsthalf - b.firsthalf

def suffixArray(s):
	N = len(s)

	suffix_rank = [[0 for i in range(N)] for j in range(N)]
	for i in range(N):
		suffix_rank[0][i] = ord(s[i]) - ord('a')

	L = [myTuple(i) for i in range(N)]

	t = 1
	step = 1
	while t < N:
		for i in range(N):
			L[i].firsthalf = suffix_rank[step - 1][i]
			if i + t < N:
				L[i].secondhalf = suffix_rank[step-1][i+t]
			else:
				L[i].secondhalf = -1
			L[i].originalindex = i
		
		L.sort(compare)
		for l in L: print l
		suffix_rank[step][L[0].originalindex] = 0

		currRank = 0
		for i in range(1,N):
			if L[i-1].firsthalf != L[i].firsthalf or L[i-1].secondhalf != L[i].secondhalf:
				currRank += 1

			suffix_rank[step][L[i].originalindex] = currRank

		t *= 2
		step += 1
	return [l.originalindex for l in L]



# Z-Function

def z(s):
    n = len(s)
    z = [0]*n
    l,r = 0,0
    for i in range(n):
        if i<=r:
            z[i] = min(r-i +1, z[i-l])
        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            l = i
            r = i+z[i]-1
    return z


# LCP array - Largest common prefix

def LCP(s):
    n = len(s)
    sA = suffixArray(s)
    k = 0
    lcp = [0 for i in range(n)]
    rank = [0 for i in range(n)]
    for i in range(n):
        rank[sA[i]] = i
    for i in range(n):
        if rank[i] == n-1:
            k = 0
            continue

        j=sA[rank[i]+1]
        while i+k<n and j+k<n and s[i+k]==s[j+k]:
            k += 1
        lcp[rank[i]] = k  
        
        if k:
            k -= 1
        else:
            k = 0
    #lcp[n-1] = n
    return sA,lcp
