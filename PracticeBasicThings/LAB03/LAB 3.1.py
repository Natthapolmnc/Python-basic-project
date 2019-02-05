F=open("Vote.txt" , "r")
A=(F.readline()).strip()
B=(F.readline()).strip()
C=(F.readline()).strip()
D=(F.readline()).strip()
E=(F.readline()).strip()
n=("")
Y= 0
X= 0
Z= 0
F.close()
if A=="A":
    Y+=1
elif A=="B":
    Z+=1
elif A=="C":
    X+=1
if B=="A":
    Y+=1
elif B=="B":
    Z+=1
elif B=="C":
    X+=1     
if C=="A":
    Y+=1
elif C=="B":
    Z+=1
elif C=="C":
    X+=1
if D=="A":
    Y+=1
elif D=="B":
    Z+=1
elif D=="C":
    X+=1
if E=="A":
    Y+=1
elif E=="B":
    Z+=1
elif E=="C":
    X+=1
if Y>=3:
    print ("A win")
    n=("A win")
elif X>=3:
    print ("C win")
    n= ("C win")
elif Z>=3 :
    print ("B win")
    n= ("B win")
else: 
    print ("No win")
print (X)
print (Y)
print (Z)
K=open('output.txt', 'w')
n1=K.write(n)
