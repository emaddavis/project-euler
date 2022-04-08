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

prob6()