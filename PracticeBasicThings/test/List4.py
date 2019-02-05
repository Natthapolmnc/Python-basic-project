def absvec(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum**0.5
u=[1.00,0.00,1.00,0.00,0.00,1.00]
v=[2.00,4.00,6.00,8.00,10.00,12.00,14.00]
print (absvec(u)*absvec(v))