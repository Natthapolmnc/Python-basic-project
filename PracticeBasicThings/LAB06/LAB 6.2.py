n=int(input("Number of students :"))
print ("Enter scores for", n,"students")
A=B=C=D=F=0
for i in range(n):
    Score=int(input())
    if Score<=60:
         A+=1
    elif Score<=70:
         B+=1
    elif Score<=80:
         C+=1
    elif Score<=90:
         D+=1
    elif Score<=100:
         F+=1
print ("Histrogram:\n0- 60:",A,"\n61-70:",B,"\n71-80:",C,"\n81-90:",D,"\n91-100:",F,)