def fibonacci(n, memo={}):
    if n in memo:
        return memo[n] #n memo dotor oldvl butsaasnar dahin tootsolhgua
    if n <= 1: #0 esul 1 bvl fibonnaciin daralld uursdihn utga bdg blhor shuud butsaana
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(0)) 
print(fibonacci(1))  
print(fibonacci(10))  
print(fibonacci(20))  
