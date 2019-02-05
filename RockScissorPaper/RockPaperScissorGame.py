print ("S for scissors\nP for paper\nR for rock ")
P1=input("Player A:")
if P1 == "S" or P1=="P" or P1=="R" :
    P2= input("Player B:")
    if P2 == "S" or P2=="P" or P2=="R" :
        if P1==P2:
            print ("tie")
        elif (P1=="S" and P2=="P") or (P1=="P" and P2=="R") or (P1=="R" and P2=="S"):
            print ("A WIN")
        else:
            print ("B WIN")
    else:
        print ("INVALID INPUT")
else:
    print ("INVALID INPUT")