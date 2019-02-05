Z=0
Y=0
print ("Enter number of items & price :")
while 1==1 :
 ea=input()
 if ea != "E":
  price=int(input())
  Z=Z+(int(ea)*price)
  Y=Y+int(ea)
 elif ea == "E":
     break
print (Y,"items for",Z,"Bahts")