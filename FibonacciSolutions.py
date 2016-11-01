def FibonacciUsingRecursion(n):
    
    # Base case
    if n == 0 or n == 1:
        return n
    else:
        # Recurse
        return FibonacciUsingRecursion(n-1) + FibonacciUsingRecursion(n-2)

def FibonacciUsingIteration(n):
    
    previousNumber = 0
    sum = 1
    
    for i in range(1,n): 
        sum += previousNumber
        previousNumber = sum - previousNumber
    return sum

# 0, 1, 1, 2, 3, 5
# a,b = b,a+b
# 0,1 = 1,1
# b,c = c,b+c
# 1,1 = 1,2
# c,d = d,c+d
# 1,2 = 2,3

def fib_iter(n):
    
    a,b = 0,1
    
    for i in range(n):
        
        a,b = b,a+b
    
    return a
