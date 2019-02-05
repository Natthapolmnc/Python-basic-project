f=open("score.txt","a")
n=int(input("Number of student:"))
if n==1 :
    print ("Enter scores for", n,"student:")
else:
    print ("Enter scores for", n,"students:")
sum=0
for i in range(n):
    score=float(input())
    f.write(str(score)+"\n")
    sum+=score
mean=sum/n
f.write("average = "+ str(mean))
f.close()