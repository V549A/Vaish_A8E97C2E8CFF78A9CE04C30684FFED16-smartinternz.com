#p factorial of a even numbers
def fact(n):
  if n == 0:
    return 1
  else:
    return n*fact(n-1)
print(fact(0))
print(fact(7))