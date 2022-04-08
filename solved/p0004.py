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