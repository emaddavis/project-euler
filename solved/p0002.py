def prob2():
    x, y = 1, 1
    result=0
    limit = 4000000

    while x<limit:
        x, y = y, x+y
        if x%2==0 and x<limit:
            result += x

    print(result)

prob2()  