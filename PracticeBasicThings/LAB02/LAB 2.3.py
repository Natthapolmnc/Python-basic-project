import re

print ("Enter you student ID: ")
ID=input()
pattern= r"61......23"

if re.match(pattern, str(ID)):
 print ("Sci Freshie")
else:
 print ("NOT Sci Freshie")
