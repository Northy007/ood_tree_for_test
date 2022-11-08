class Node: 
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,node,data):
        if node is None :               #ตัวแรกคือ root ถ้า root ว่าง node นั้นก็จะกลายเป็น root
            return Node(data)
        if data < node.data :
            node.left = self.insert(node.left,data) #ถ้า insert เข้ามาแล้ว node นั้นไม่ว่างให้เลื่อนไปกิ่งใดกิ่งหนึ่ง
        if data > node.data :
            node.right = self.insert(node.right,data)
        return node

    def delete(self,node,data):
        if node is None :
            return node
        if data < node.data :
            node.left = self.delete(node.left,data)
        if data > node.data :
            node.right = self.delete(node.right,data)
        else : # data = node.data

            # สำหรับ node ที่มี node child เดียวหรือไม่มี
            if node.left is None :
                temp = node.right
                node = None
                return temp

            if node.right is None :
                temp = node.left
                node = None
                return temp

            # สำหรับ node ที่มี two child node ค่าน้อยสุดของ node นั้นขึ้น
            temp = self.min(node.right)

            node.data = temp.data
            node.right = self.delete(node.right,temp.data)            
        return node    


    def min(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def max(self,node) :
        while node.right is not None :
            node = node.right
        return node 

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

Tree = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
    Tree.root = Tree.insert(Tree.root,i)

Tree.printTree(Tree.root)
Tree.root = Tree.delete(Tree.root,2)
print("----------------------------------")
Tree.printTree(Tree.root)

