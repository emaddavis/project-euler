################################################################################
def prob7():
    target = 10001
    print(nth_prime(target))

def nth_prime(target):
    prime_list = []
    leading_prime = 2
    seed = 2
    length = len(prime_list)

    while(length < target):
        prime_state = is_prime(seed)

        if(prime_state):
            leading_prime = seed
            prime_list.append(leading_prime)

        length = len(prime_list)
        seed += 1

    return leading_prime 

def is_prime(m):
    x = 2
    n = m

    while x * x <= n:
        while n%x==0:
            n=n/x
        x += 1
    return(n == m)
prob7()
################################################################################
def prob6():
    low = 1
    high = 100
    result = square_of_sums(low, high) - sum_of_squares(low, high)
    print(result)

def square_of_sums(low, high):
    high += 1
    x_range = range(low, high)
    result = 0

    for x in x_range:
        result += x
    
    result = result * result
    return result

def sum_of_squares(low, high):
    high += 1
    x_range = range(low, high)
    result = 0

    for x in x_range:
        y = x * x
        result += y

    return result

#prob6()
################################################################################
def prob5():
    result = 11*13*14*17*18*19*20
    print(result)

#prob5()
################################################################################
def prob4():
    result = []
    for i in range(1000):
        for j in range(1000):
            product = i*j
            if is_palindrom(product):
                result.append(product)
    print(max(result))

def is_palindrom(n):
    result = True
    n = str(n)
    array = list(n)
    length = int(len(array)/2)
    count = 0
    while count < length and result:
        first = 0
        last = -1

        if (array[first+count] !=  array[last-count]):
            result = False
        
        count += 1
    
    return result

#prob4()
################################################################################
def prob3():
    n = 600851475143
    x = 2

    while x * x <= n:
        while n%x==0:
            n=n/x
        x += 1
    print(n)
#prob3()
################################################################################
def prob2():
    x, y = 1, 1
    result=0
    limit = 4000000

    while x<limit:
        x, y = y, x+y
        if x%2==0 and x<limit:
            result += x

    print(result)

#prob2()    
################################################################################
def prob1():
    x = range(1,1000)
    mod_sum = 0
    for i in x:
        if(i%3==0 or i%5==0):
            mod_sum = mod_sum + i
    
    print(mod_sum)
            
#prob1()
################################################################################

