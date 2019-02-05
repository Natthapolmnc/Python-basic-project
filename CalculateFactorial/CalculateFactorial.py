def factlist(number):
    fact=1
    factlist=[1]
    for i in range(1,number):
        fact=fact*i
        factlist+=[fact]
    return factlist
n=int(input("fact number:"))
print(factlist(n))