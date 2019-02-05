year=depos=1
while 1==1:
    depos=float(input("Enter deposite amount:"))
    if depos<500:
        break
    while year<=5:
        if year!=3:
            depos+=(depos*0.1)
            year+=1
        elif year==3:
            print ("After 3 years, Mom gives you :", depos*0.05)
            depos+=-(depos*0.05)
            print ("Your current money", depos)
            year+=1
            continue
    year=1
    print ("After 5 years, your total money is", depos)