n=int(input("Enter n :"))
Fibo0=0
Fibo1=1
Fibo=0
for i in range(n-1):
    Fibo=Fibo1+Fibo0
    Fibo0=Fibo1
    Fibo1=Fibo
    i+=1
print (Fibo)