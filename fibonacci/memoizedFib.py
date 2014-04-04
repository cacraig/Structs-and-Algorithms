class Fib:
  def __init__(self):
    self.callCtr = 0
    self.cache = {}

  def fib(self, n):
    # Track number of calls.
    # For complexity analysis
    self.callCtr += 1
    if n <= 1:
      return n

    if n in self.cache:
      return self.cache[n]
    else:
      self.cache[n] = self.fib(n-2) + self.fib(n-1)
      return self.cache[n]      

fibClass = Fib()
num = fibClass.fib(5)
print "5th Fibonacci Number: " + str(num) + " number of calls: " + str(fibClass.callCtr)

fibClass = Fib()
num = fibClass.fib(12)
print "12th Fibonacci Number: " + str(num) + " number of calls: " + str(fibClass.callCtr)

fibClass = Fib()
num = fibClass.fib(36)
print "36th Fibonacci Number: " + str(num) + " number of calls: " + str(fibClass.callCtr)

fibClass = Fib()
num = fibClass.fib(1000)
print "1000th Fibonacci Number: " + str(num) + " number of calls: " + str(fibClass.callCtr)
