def fact(start, end) :
    f = 1
    for x in range(start, end+1) :
        f *= x
        
    return f

def inc_10(x) :
    x += 10
    return x

def mul_20(x) :
    return x*20