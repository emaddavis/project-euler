def prob1():
    x = range(1,1000)
    mod_sum = 0
    for i in x:
        if(i%3==0 or i%5==0):
            mod_sum = mod_sum + i
    
    print(mod_sum)
            
prob1()