class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def addNode(self, data):
    node = Node(data)

    # list is empty, set head to new node.
    if self.head == None:
      self.head = node

    # if linked list not empty, set tail.next = new node   
    if self.tail != None:
      self.tail.next = node

    # regardless, set the last to the new node.
    self.tail = node
    
  def removeNode(self, idx):
    prev = None
    # initialize first node for search.
    node = self.head
    i = 0

    while (node !=None) and (i<idx):
      prev = node
      node = node.next
      i += 1

    # Element of idx should not be set in node variable.
  
    # if there is no previous element, the list has only one element.
    # Set the head to point to the only element in list.  
    if prev == None:
      self.head = node.next
    else:
      # This breaks the pointers (and removes the element)
      # Previous.next(the current element) 
      # is now node.next (the next element after element of idx position)
      prev.next = node.next

  def printList(self):
    node = self.head
    while node != None:
      print node.data
      node = node.next

linkedList = LinkedList()

linkedList.addNode('Colin')
linkedList.addNode('Craig')

linkedList.printList()

linkedList.removeNode(1)

linkedList.printList()
