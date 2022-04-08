from itertools import combinations, count
from functools import reduce

def trianglenums():
    for n in count(start=1, step=1):
        yield n * (n + 1) // 2

def factoring(n):
    divs = [1]
    i = 2
    while n > 1:
        while not n % i:
            n /= i
            divs.append(i)
        i += 1
    return divs

def divisors(n):
    divs = factoring(n)
    primes = divs[1:]

    for j in range(1, len(primes)):
        for comb in combinations(primes, j + 1):
            newdiv = reduce(lambda x, y: x*y, comb)
            if newdiv <= n and newdiv not in divs:
                divs.append(newdiv)
    return len(divs)


for i in trianglenums():
    if divisors(i) > 500:
        print(i)
        break

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n ** 0.5) + 1) if not n % i)))

print(factors(500))
