temp=[32.5, 33, 34.5, 36, 35, 35.5, 34]
temp1=[]
for i in range(len(temp)):
    if temp[i]>=35:
        temp1+=[temp[i]]
print (len(temp1))