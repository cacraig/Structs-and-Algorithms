class Node:
  def __init__(self, data = None, left = None, right = None):
    '''''
    A root node of a tree has at most two children, and it's data value.
    '''''
    self.data = data
    self.left = left
    self.right = right
  
  def insert(self, data):
    '''''
    Insert data into tree. If data is less than current node's data,
      set left child. If left child is set, make recursive calls checking left/right
      children until a spot is found. (vice versa for right)
    '''''
    if data < self.data:
      if self.left == None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    else:
      if self.right == None:
        self.right = Node(data)
      else:
        self.right.insert(data)
  
  def find(self, data, parent=None):
    '''''
    Traverse the tree, and check left/right children until either the same value is found,
      or the value is not found at all.
    '''''
    if data < self.data:
      if self.left is None:
        return None, None
      return self.left.find(data, self)

    elif data > self.data:
      if self.right is None:
        return None, None
      return self.right.find(data, self)
    else:
      return self, parent

  def printTree(self):
    '''''
    Print tree inorder -- Breadth first.
      We first traverse the left subtree, then we print the root node then we traverse the right subtree.
    '''''
    if self.left:
      self.left.printTree()
    print self.data
    if self.right:
      self.right.printTree()


root = Node(8)
root.insert(7)
root.insert(2)
root.insert(9)

print root.find(4)
foundNode, parent = root.find(9)

print "Found! Value: " + str(foundNode.data) + " with parent " + str(parent.data)

root.printTree()
