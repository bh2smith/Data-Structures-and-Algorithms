class ThreeDFenwick():
    
    def __init__(self,N):
        self.l = N
        self.t = [[[0 for x in range(N+1)] for y in range(N+1)] for z in range(N+1)] 
        
    def add(self, x,y,z,v):
        i = x
        while i <= self.l:
            j = y
            while j <= self.l:
                k = z
                while k <= self.l:                   
                    self.t[i][j][k] += v               
                    k |= k+1
                j |= j+1
            i |= i+1
    
    def Sum(self,x,y,z):
        tot = 0
        i = x
        while i >= 0:
            j = y
            while j >= 0:
                k = z
                while k >= 0:
                    tot += self.t[i][j][k]
                    k = (k&(k+1)) - 1
                j = (j&(j+1)) - 1
            i = (i&(i+1)) - 1
        return tot
    
    def update(self,x,y,z,v):
        self.add(x,y,z,v-self.t[x][y][z])
        
    def query(self, x1,y1,z1, x,y,z):
        val1 = self.Sum(x,y,z)-self.Sum(x1-1,y,z)-self.Sum(x,y1-1,z)+self.Sum(x1-1,y1-1,z)
        val2 = self.Sum(x,y,z1-1)-self.Sum(x1-1,y,z1-1)-self.Sum(x,y1-1,z1-1)+self.Sum(x1-1,y1-1,z1-1)
        return val1 - val2
