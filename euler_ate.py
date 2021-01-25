import time
import math
from functools import reduce
from itertools import combinations, count
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
#prob10()
#################################################################################
def prob11():
    raw_matrix = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

    matrix = convert_text_to_int_matrix(raw_matrix)
    largest = 0

    #horizontal
    for i in range(0,(len(matrix))):
        for j in range(0,(len(matrix[i])-3)):
                a = matrix[i][j]
                b = matrix[i][j+1]
                c = matrix[i][j+2]
                d = matrix[i][j+3]
                n = a*b*c*d
                if n>largest:
                    largest = n

    #vertical
    for i in range(0,(len(matrix)-3)):
        for j in range(0,(len(matrix[i]))):
                a = matrix[i][j]
                b = matrix[i+1][j]
                c = matrix[i+2][j]
                d = matrix[i+3][j]
                n = a*b*c*d
                if n>largest:
                    largest = n
    
    #diagonal_up
    for i in range(3,(len(matrix)-3)):
        for j in range(0,(len(matrix[i])-3)):
                a = matrix[i+3][j]
                b = matrix[i+2][j+1]
                c = matrix[i+1][j+2]
                d = matrix[i][j+3]
                n = a*b*c*d
                if n>largest:
                    largest = n
    
    #diagonal_down
    for i in range(3,(len(matrix)-3)):
        for j in range(0,(len(matrix[i])-3)):
                a = matrix[i][j+3]
                b = matrix[i+1][j+2]
                c = matrix[i+2][j+1]
                d = matrix[i+3][j]
                n = a*b*c*d
                if n>largest:
                    largest = n

    print(largest)

def convert_text_to_int_matrix(raw_matrix):
    text_matrix_line = raw_matrix.split("\n")
    text_matrix = []
    for i in text_matrix_line:
        text_matrix.append(i.split())
    
    matrix = []
    for i in range(0, len(text_matrix)):
        row = []
        for j in range(0, len(text_matrix[i])):
            row.append(int(text_matrix[i][j]))
        matrix.append(row)

    return matrix

#prob11()
#################################################################################
def prob12():
    divisors = []
    limit = 500
    count = 1
    while len(divisors) <= limit:
        divisors = []
        for i in range(1,(count+1)):
            if count % i == 0:
                divisors.append(i)
        if len(divisors) >= limit:
            print(count)
        count += 1
    
    print(t2-t1)

#prob12()
#################################################################################
def prob12a():
    count = 1
    array = []
    while len(array) < 10:
        array.append(count)
        print(sum(array))
        count += 1

def get_divisors(number):
    divisors = []
    count = 1
    while count <= number:
        if number % count == 0:
            divisors.append(count)
    return divisors 

#get_divisors(28)
#prob12a()
#################################################################################
def prob12b():
    triangle_summands = [1]
    triangle_factors = []

    while len(triangle_factors) < 500:
        triangle_summands.append(triangle_summands[-1] + 1)
        triangle_factors = get_factors(sum(triangle_summands))
        print(triangle_summands)
        print(len(triangle_factors))

def get_factors(number):
    factors = []
    for n in range(1, number+1):
        if number % n == 0:
            factors.append(n)
    return factors

#prob12b()
#################################################################################
def prob12e():
    leading_triangle_number = 1
    step = 2
    triangle_factors = []
    toggle = True
    while toggle:
        leading_triangle_number = leading_triangle_number + step
        step += 1
        triangle_factors = get_factors(leading_triangle_number)
        #print(triangle_factors)
        #print(leading_triangle_number)
        print(len(triangle_factors), leading_triangle_number)
        if (len(triangle_factors) > 500):
            print(leading_triangle_number)
            toggle = False
        
#prob12e()

def play():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 20, 21, 24, 28, 30, 35, 40, 42, 56, 60, 70, 84, 105, 120, 140, 168, 210, 280, 420, 840]
    print(len(arr))

play()
