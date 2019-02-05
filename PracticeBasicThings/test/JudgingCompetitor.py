J1=input("Judge #1:")
J2=input("Judge #2:")
J3=input("Judge #3:")
J4=input("Judge #4:")
J5=input("Judge #5:")
x=y=0
if J1 == "A":
    x+=1
if J2 == "A":
    x+=1
if J3 == "A":
    x+=1
if J4 == "A":
    x+=1
if J5 == "A":
    x+=1
if x>2 :
    print("A WIN")
else:
    print("B WIN")