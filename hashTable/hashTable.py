class KeyVal:
  def __init__(self, key, val):
    self.key = key
    self.val = val

class HashTable:
  SIZE = 10
  # Initialize our hash table to size SIZE
  def __init__(self):
    i = 0
    self.list = []
    while i<self.SIZE:
      self.list.append([])
      i += 1

  def getValue(self, key):
    '''''
    Gets hash, locates bucket, and finds key-val set in that bucket (if it exists)
    '''''
    h = self.hash(key)
    bucket = self.list[h]
    for kv in bucket:
      if kv.key == key:
        return kv.val

  def setValue(self, key, val):
    '''''
    Adds a Key-val pair to bucket self.list[h].
    '''''
    h = self.hash(key)
    bucket = self.list[h]
    bucket.append(KeyVal(key, val))

  def remove(self, key):
    '''''
    Does the same thing as getValue, but removes also.
    '''''
    h = self.hash(key)
    bucket = self.list[h]
    for kv in bucket:
      if kv.key == key:
        self.list[h].remove(kv)

  def hash(self, key):
    '''''
    HASH FUNCTION
      HASH = (ASCII value of key) % SIZE

    HASH is the index of the bucket into which things go.
    '''''
    i = 0
    total = 0
    while i < len(key):
      total = total + ord(key[i])
      i += 1
    return total % self.SIZE    
    

hashTable = HashTable()
hashTable.setValue('name', 'Craig')
hashTable.setValue('phone', '910-545-1995')
hashTable.setValue('location', 'Your mom')

print hashTable.getValue('name')
print hashTable.getValue('phone')
print hashTable.getValue('location')

key ='name'
print "Removing key: " + key
print hashTable.remove('name')
print hashTable.getValue('name')
