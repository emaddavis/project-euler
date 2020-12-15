import math 
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
def prob5():
    result = 11*13*14*17*18*19*20
    print(result)

#prob5()
#################################################################################
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
#prob7()
###############################################################################
def prob8():
    adjacent_digit_length = 13

    dirty_string = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
    
    number_as_string = dirty_string.replace("\n","")

    number_char_list = list(number_as_string)

    number_list = []

    for n in number_char_list:
        number_list.append(int(n))
    
    length = len(number_list)

    products = []
    
    i = 0
    while i <= length - adjacent_digit_length:
        running_array = []
        j = 0
        while j < adjacent_digit_length:
            running_array.append(number_list[i+j])
            j += 1
        products.append(product_of_array(running_array))
        i += 1

    print(max(products))




def product_of_array(array):
    product = 1
    for a in array:
        product = product * a
    return product

    
#prob8()
################################################################################
def prob9():
    for a in range(1,500):
        for b in range(1,500):
            c = math.sqrt(a**2 + b**2)
            if  a + b + c == 1000:
                return (a*b*c)
#print(prob9())
#################################################################################
def prob10():
    limit =  2000000
    primes_below = []
    for i in range(2,limit):
        if is_prime(i):
            primes_below.append(i)
    print(sum(primes_below))
prob10()
#################################################################################
