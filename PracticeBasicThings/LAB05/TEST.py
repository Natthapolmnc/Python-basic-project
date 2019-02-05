num=int(input())
min=max=num
for i in range(14):
    num=int(input())
    if num<min:
        min=num
    if num>max:
        max=num
print (max,min)