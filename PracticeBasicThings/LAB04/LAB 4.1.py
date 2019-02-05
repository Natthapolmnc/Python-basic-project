N=open('order.txt', 'r')
K=int(N.readline().strip())
Z= 0
for i in range(K):
 Z=Z+float(N.readline().strip())
print (Z)
