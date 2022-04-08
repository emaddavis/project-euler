import math
import time

def prob9():
    time_time = time.time()
    for a in range(1,500):
        for b in range(1,500):
            c = math.sqrt(a**2 + b**2)
            if  a + b + c == 1000:
                print(time.time() - time_time)
                return (a*b*c)
print(prob9())