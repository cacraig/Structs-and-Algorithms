def reverse(str):
  head_ptr = 0
  tail_ptr = len(str) - 1
  while(head_ptr < tail_ptr/2):
    head = str[head_ptr]
    tail = str[tail_ptr]
    
    str[head_ptr] = tail
    str[tail_ptr] = head
    head_ptr = head_ptr + 1
    tail_ptr = tail_ptr - 1
  return ''.join(str)

print reverse(list("colin"))
