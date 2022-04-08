def prob3():
    n = 600851475143
    x = 2

    while x * x <= n:
        while n%x==0:
            n=n/x
        x += 1
    print(n)
    
prob3()