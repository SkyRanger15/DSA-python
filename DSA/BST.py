class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, value):
        if value < self.val:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert(value) 

# tree = TreeNode(10)
# tree.insert(5)
# tree.insert(4)
# tree.insert(2)
# tree.insert(1)
# tree.insert(3)
# tree.insert(22)
# tree.insert(11)
# tree.insert(12)

# print(tree.left.left.left.right.val)



    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print (self.val)
        if self.right:
            self.right.inorder_traversal()



    def preorder_traversal(self):
        print (self.val)
        if self.left:
            self.left.preorder_traversal()
        
        if self.right:
            self.right.preorder_traversal()


    def postorder_traversal(self):
        
        if self.left:
            self.left.postorder_traversal()
        
        if self.right:
            self.right.postorder_traversal()
        print (self.val)



    def find(self, value):
        if value < self.val:
            if not self.left:
                return False
            else:
                return self.left.find(value)
        elif value > self.val:
            if not self.right:
                return False
            else:
                return self.right.find(value)
        else:
            return True
    





tree = TreeNode(6)
n =int(input("Enter No of Nodes: "))
for i in range(n):
    ele = int(input(f"enter node {i+1} value:  "))
    tree.insert(ele)

tree.inorder_traversal()

fin = int(input("Enter the element to find: "))

if tree.find(fin):
    print("Element Found")
else:
    print("Element Not Found")
