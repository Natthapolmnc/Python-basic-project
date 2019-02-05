Q= str(input())
W= str(input())
E= str(input())
R= str(input())
T= str(input())
if Q == "a":
    Y=1
else:
    Y=0
if W == "a":
    U=1
else:
    U=0
if E == "a":
    I=1
else:
    I=0
if R == "a":
    O=1
else:
    O=0
if T == "a":
    P=1
else:
    P=0
Sum= Y+U+I+O+P
if Y == 1:
    print ("Judge #1: A")
else:
    print ("Judge #1: B")
if U == 1:
    print ("Judge #2: A")
else:
    print ("Judge #2: B")
if I == 1:
    print ("Judge #3: A")
else:
    print ("Judge #3: B")
if O == 1:
    print ("Judge #4: A")
else:
    print ("Judge #4: B")
if P == 1:
    print ("Judge #5: A")
else:
    print ("Judge #5: B")
if Sum < 3:
    print ("The winner is contestant B.")
else:
    print ("The winner is contestant A.")
