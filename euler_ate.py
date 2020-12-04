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

prob4()
################################################################################
def prob3():
    n = 600851475143
    x = 2

    while x * x < n:
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

