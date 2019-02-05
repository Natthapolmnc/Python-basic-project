K=open('problem.txt', 'r')
L=open('solutions.txt', 'w')
L.close()
Z=open('solutions.txt', 'a')
def quad1(a, b, c) :
    if ((b**2-(4*a*c))>=0):
        A= ((-b+(b**2-(4*a*c))**0.5)/(2*a))
        n1 = Z.write(str(A)+"\n")
    else:
      n2 = Z.write("invalid input\n")

def quad2(a, b, c) :
    if ((b**2-(4*a*c))>=0) :
        B= ((-b-(b**2-(4*a*c))**0.5)/(2*a))
        n1 = Z.write(str(B)+"\n")
    else:
      n2 = Z.write("invalid input\n")

for i in range(4) :
 N= K.readline().split()
 quad1(float(N[0]), float(N[1]), float(N[2]))
 quad2(float(N[0]), float(N[1]), float(N[2]))
K.close()

    