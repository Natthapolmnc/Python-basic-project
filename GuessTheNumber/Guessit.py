import random as r
print("Guess a number between 1-3 ")
k=0
while k<=1 :
    n=int(input("Enter a number : "))
    p=r.randint(1,3)
    print("Randomed by computer : ",p)
    if n==p:
       print("Correct")
       k=k+1
       if k==2:
           print("you win")
    if n!=p:
       print("Wrong")
       k=0
