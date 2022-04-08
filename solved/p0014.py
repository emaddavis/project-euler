import helper as h

def collatz(n:int):
    sequence = []
    sequence.append(int(n))
    while n != 1:
        if h.is_even(n):
            n = n/2
        else:
            n = 3*n+1
        sequence.append(int(n))
    #print(sequence) #uncomment to make sure you're calcing collatz properly 
    #print(len(sequence)
    return sequence

min = 1
max = 1000000
max_len = {"n":0, "len":0}
for i in range(min,max+1):
    current_len = len(collatz(i))
    if (current_len > max_len["len"]):
        max_len["n"] = i
        max_len["len"] = current_len

print(f'''{max_len['n']} is the creates the longest Collatz sequence under 1 million with {max_len['len']} numbers''')

