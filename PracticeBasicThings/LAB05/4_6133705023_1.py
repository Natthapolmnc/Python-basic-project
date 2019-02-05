amount=0
total=0
box=0
while box<5:
    amount=int(input("Enter amount : "))
    if amount<=0 :
        break
    total=total+amount
    box=total//12
print("Total amount = ",total)
print("Total boxes = ",box)
