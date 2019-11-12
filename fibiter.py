def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return b    
        
def p(x):
    for i in range(x):
        print(fib(i))

p(50)
