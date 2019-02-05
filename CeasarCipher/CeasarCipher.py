c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher=""
message,d=input("Enter message and distance:").split()
for i in range(len(message)):
    j=0
    while(message[i]!=c[j]):
        j+=1
    cipher=cipher+c[(j+int(d))%26]
print("Cipher Text:",cipher)