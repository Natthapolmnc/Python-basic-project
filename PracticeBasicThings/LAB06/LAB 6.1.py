n=int(input())
New=open("score1.txt", "w")
New.close
J=0
O=open("score1.txt", "a")
print ("Enter scores for", n,"students")
for i in range(n):
    a=input()
    J=J+int(a)
    SIT=str(J/n)
    L=O.write(a)
    L=O.write("\n")
L=O.write("Average=")
L=O.write(SIT)
