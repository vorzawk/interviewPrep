# Reduce a problem into a simpler version of the same problem. Keep going until the problem is so simple that the answer is trivial. 
# And then, just recursion take care of the rest.

def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def isPal(s):
    # Expects s to only contain lowercase letters
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and isPal(s[1:-1])



        


