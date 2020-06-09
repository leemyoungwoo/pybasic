a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = a.index(30)
print(x)

a.pop(x)     # del a[x]와 동일
print(a)

a.remove(90)
print(a)

a.clear()
print(a)