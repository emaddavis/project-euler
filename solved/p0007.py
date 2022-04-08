import helper as h
def prob7():
    target = 10001
    print(nth_prime(target))

def nth_prime(target):
    prime_list = []
    leading_prime = 2
    seed = 2
    length = len(prime_list)

    while(length < target):
        prime_state = h.is_prime(seed)

        if(prime_state):
            leading_prime = seed
            prime_list.append(leading_prime)

        length = len(prime_list)
        seed += 1

    return leading_prime 

prob7()