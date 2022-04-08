def is_prime(m):
    x = 2
    n = m

    while x * x <= n:
        while n%x==0:
            n=n/x
        x += 1
    return(n == m)

def int_len(num:int):
    return len(str(num))

def is_even(num:int):
    if num%2==0:
        return True
    else:
        return False