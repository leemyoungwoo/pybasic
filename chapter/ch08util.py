def facto(n):
    if n == 0 :
        return 1
    return n*facto(n-1)
    
def fibo(n) : 
    if n == 1 or n ==2 :
        return 1
    return fibo(n-1) + fibo(n-2)