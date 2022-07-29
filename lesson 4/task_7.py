def fact(n):
    acc = 1
    for i in range(1,n+1):
        acc*=i
        yield acc

for el in fact(10):
    print(el)