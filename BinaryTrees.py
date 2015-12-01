#####################################
# Binary Tree and Binary Search Tree


class BinaryTree():

    def __init__(self,data = None):
        self.root = data
        self.left = None
        self.right = None
        self.parent = None
    def getRoot():
        return self.root
    def hasLeft(self):
        return self.left != None
    def hasRight(self):
        return self.right != None
    def isLeft(self):
        return self.parent != None and self.parent.left == self
    def isRight(self):
        return self.parent != None and self.parent.right == self
    def isRoot(self):
        return self.parent == None
    def isLeaf(self):
        return self.right == None and self.left == None
    def hasAnyChildren(self):
        return self.right != None or self.left != None
    def hasBothChildren(self):
        return self.right != None and self.left != None
    def inOrder(self): #LCR
        s = []                
        if self.hasLeft():
            s += self.left.inOrder()
        s.append(self.root)
        if self.hasRight():
            s += self.right.inOrder()
        return s

    def preOrder(self): # CLR   
        s = [self.root]
        if self.hasLeft():
            s += self.left.preOrder()
        if self.hasRight():
            s += self.right.preOrder()
        return s
        
    def postOrder(self): #LRC
        s = []            
        if self.hasLeft():
            s += self.left.postOrder()
        if self.hasRight():
            s += self.right.postOrder()
        s.append(self.root)
        return s

    def length(self):
        if self.isLeaf():
            return 1
        else:
            if not self.hasLeftChild():
                return 1+ self.right.length()
            else:
                return 1 + max(self.left.length(), self.right.length())

    def diameter(self):
        if self.isLeaf():
            return 1
        if not self.hasLeftChild():
            return max(self.length(), 1+self.right.diameter())
        else:
            return max(1+self.left.diameter(),1+self.right.diameter(), self.left.length() + self.right.length()+1)

class BinarySearchTree(BinaryTree):
    def __init__(self,data = None):
        BinaryTree.__init__(self,data)
        self.height = 0
        
    def insert(self,data):
        if self.root == None:
            self.root = data
            self.height = 1
        elif self.root == data:
            return
        else:
            if data < self.root:            
                if self.hasLeft():
                    self.left.insert(data)
                else:
                    self.left = BinarySearchTree(data)
            else:
                if self.hasRight():
                    self.right.insert(data)
                else:
                    self.right = BinarySearchTree(data)           
            self.updateHeight()

    def updateHeight(self):
        if self.hasBothChildren():
            self.height = max(self.left.height, self.right.height) + 1              
        elif self.hasLeft():
            self.height = self.left.height + 1
        elif self.hasRight():
            self.height = self.right.height + 1
    
    def bal(self):        
        if self.hasBothChildren():
            return self.left.height - self.right.height
        elif not self.hasAnyChildren():
            return 0
        elif self.hasLeft():
            return self.left.height
        else:
            return - self.right.height

    def rightRotate(self):
        newroot = self.left
        self.left = newroot.right
        newroot.right = self
        self.height = max(self.left.height, self.right.height) + 1
        newroot.height = max(newroot.left.height, newroot.right.height) + 1
        return newroot

    def leftRotate(self):
        newroot = self.right
        self.right = newroot.left
        newroot.left = self
        self.height = max(self.left.height, self.right.height) + 1
        newroot.height = max(newroot.left.height, newroot.right.height) + 1
        return newroot

    def isBalanced(self):
        return -1<=self.bal()<=1
    
    def end(self):
        if self.hasRight():
            return self.right.end()
        return self.root
    
    def lowerBound(self,x):
        v = self.root
        if v == x-1:
            return v     
        if v>=x:
            if self.hasLeft():
                return self.left.lowerBound(x)
            else:
                return -1
        else:
            if self.hasRight():
                return self.right.lowerBound(x)
            else:
                return -1

    def balance(self):
        b = self.bal()
        if b >1:
            if self.left.isBalanced() and self.right.isBalanced():
                if self.left.left.height >= self.left.right.height:
                    self.rightRotate()
                else:
                    self.left = self.left.leftRotate()
                    self.rightRotate()
            else:
                self.left.balance()

        if b < -1:
            if self.left.isBalanced() and self.right.isBalanced():
                if self.right.right.height>=self.right.left.height:
                    self.leftRotate()
                else:
                    self.right = self.right.rightRotate()
                    self.leftRotate()
            else:
                self.right.balance()
        self.updateHeight()
