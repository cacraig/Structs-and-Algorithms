class Fib:
  def __init__(self):
    self.callCtr = 0

  def fib(self, n):
    # Track number of calls.
    # For complexity analysis
    self.callCtr += 1

    if n <= 1:
      return n
    return self.fib(n-2) + self.fib(n-1)

fibClass = Fib()
num = fibClass.fib(5)
print "5th Fibinacci Number: " + str(num) + " number of calls: " + str(fibClass.callCtr)

fibClass = Fib()
num = fibClass.fib(12)
print "12th Fibinacci Number: " + str(num) + " number of calls: " + str(fibClass.callCtr)

fibClass = Fib()
num = fibClass.fib(36)
print "36th Fibinacci Number: " + str(num) + " number of calls: " + str(fibClass.callCtr)
