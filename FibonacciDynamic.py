# Cache
n = 10
cache = [None]*(n+1)

def FibonacciDynamic(n):

    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Check Cache
    if cache[n] != None:

        return cache[n]
    else:
        # Keep Setting Cache
        cache[n] = FibonacciDynamic(n-1) + FibonacciDynamic(n-2)
        
    return cache[n]
