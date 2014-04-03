def quickSort(list):
  '''''
  Sort a string(list) operating on characters less then, and greater than the pivot char.
    Sorts asc.
  '''''
  if list == []:
    return []
  pivot = list[0]
  
  # Recursivly call. passing a subset of list from position 1->n 
  #   (excluding first char which is the pivot)
  # sort all characters that are less than the pivot character
  l = quickSort([x for x in list[1:] if x < pivot])
  # sort all characters greater than or equal to the pivot element
  u = quickSort([x for x in list[1:] if x >= pivot])
  
  # Sorted chars less than pivot + pivot char + Sorted chars greater than pivot
  return l + [pivot] + u

s = 'Colin'
print "Sorting string: " + s
print ('').join(quickSort(list(s)))

s = 'zfdklsjduiabc'
print "Sorting string: " + s
print ('').join(quickSort(list(s)))

s = 'Dog'
print "Sorting string: " + s
print ('').join(quickSort(list(s)))
