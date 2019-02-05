a=int(input("a:"))
b=int(input("b:"))
P=Pmax=1
while P<a*b:
    if (a*b)%P==1 and P>Pmax:
        Pmax=P
    P+=1
print (Pmax)
