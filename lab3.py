import random as rd
def gennumber(n):
    a= list(range(1,n+1))
    rd.shuffle(a)
    return a

class binode :
    def __init__(self,x) :
        self.x = x
        self.l = None
        self.r = None
class tree :
    def __init__(self) :
        self.root = None

    def setroot(self,root):
        self.root =root        

    def getroot(self):
        return self.root

    def addnode(self,newnode,curpos):
        if newnode.x >=curpos.x:
            if curpos.r == None:
                curpos.r = newnode
            else:
                self.addnode(newnode,curpos.r)
        else:
            if curpos.l == None:
                curpos.l = newnode
            else:
                self.addnode(newnode,curpos.l)


a = gennumber(12)
print(a)
newnode = binode(a[0])
tree1 = tree()
tree1.setroot(newnode)
root = tree1.getroot()
print(root.x)
for x in a[1:]:
    tree1.addnode(binode(x),root)

def treeheight(root):
    if root == None:
        return 0
    else:
        return max(treeheight(root.l) , treeheight(root.r)) + 1
    
print("จำนวนชั้น : ",treeheight(root))


# Preorder
preorderlist = []
def preorder(root):
    preorderlist.append(root.x)
    if root.l != None:
        preorder(root.l)
    if root.r != None:
        preorder(root.r)

preorder(root)
print("Preorderlist")
print(preorderlist)


# Inorder 
inorderlist = []
def inorder(root):
    if root.l != None:
        inorder(root.l)
    inorderlist.append(root.x)
    if root.r != None:
        inorder(root.r)
inorder(root)
print("Inorderlist")
print(inorderlist)


# Postorder
postorderlist = []
def postorder(root):
    if root is not None:
        postorder(root.l)
        postorder(root.r)
        postorderlist.append(root.x)

postorder(root)
print("Postorderlist")
print(postorderlist)
    
    



