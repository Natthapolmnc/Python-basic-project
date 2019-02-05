amount=500
while amount>=500 :
  y=1
  amount=float(input("Enter deposite amount : "))
  while amount>=500 and y<=5:
    if y!=3:
      amount=amount*1.1
    elif y==3:
      k=amount*0.05
      c=float(amount)-float(k)
      amount=c
    y=y+1
  if amount>=500:
    print("After 3 years, Mom gives you : ",k)
    print("Your current money is ",c)
    print("After 5 years, your total money is ",amount)