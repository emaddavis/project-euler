import helper as h
def prob10():
    limit =  2000000
    primes_below = []
    for i in range(2,limit):
        if h.is_prime(i):
            primes_below.append(i)
    print(sum(primes_below))
prob10()