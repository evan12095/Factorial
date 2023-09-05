# Implement a recursive function to calculate the factorial of a given number.

def factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * factorial(n-1)

num = int(input("Enter the number:"))
res = factorial(num)
print("The factorial of {} is {}".format(num,res))
