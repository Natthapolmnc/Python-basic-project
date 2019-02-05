a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
if b**2<4*a*c and a!=0:
    print ("No solution or not a quadratic eq. ")
else:
    print ("x =", (-b+(b**2-4*a*c)**0.5)/(2*a))
    print ("x =", (-b-(b**2-4*a*c)**0.5)/(2*a))