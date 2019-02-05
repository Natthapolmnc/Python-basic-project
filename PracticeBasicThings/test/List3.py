score=[35 ,24 , 36, 43, 44, 50, 50]
cal=0
for x in score:
    cal+= (x==50)
    if cal>=1:
        break
if cal>=1:
    print ("Found")
else:
    print ("Not found")