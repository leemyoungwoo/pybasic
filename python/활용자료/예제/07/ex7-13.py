def func() :
    global x
    x = 100
    print(x)
    print(id(x))
    
x = 10
print(x)
func()
print(x)
print(id(x))