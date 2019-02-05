Varie= list(float(input())for i in range(3))
Sum=(Varie[1]**2)-(4*Varie[0]*Varie[2])
if (Sum>=0):
  print ((-Varie[1]+(Varie[1]**2-4*Varie[0]*Varie[2])**0.5)/(2*Varie[0]))
  print ((-Varie[1]-(Varie[1]**2-4*Varie[0]*Varie[2])**0.5)/(2*Varie[0]))
else:
  print ("No solution or Not quadratic eq.")
  


