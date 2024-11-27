def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(0)) 
print(fibonacci(1))  
print(fibonacci(10))  
print(fibonacci(20))  
