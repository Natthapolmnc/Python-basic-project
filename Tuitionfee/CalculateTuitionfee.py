ID=int(input("Student ID:"))
sem=int(input("Semester:"))
P50= (ID//10**8)>=50 and (ID//10**8)<56
P56= (ID//10**8)>55
sem1= sem>=1 and sem<=2
sem3= sem==3
TRE=(ID//10**7)%10 != 7
Bundit= (ID//10**7)%10 == 7
Sci= ID%100==23
if TRE and sem1 and P50 and Sci:
    print ("Registration fee = 18,000")
elif TRE and sem1 and P56 and Sci:
    print ("Registration fee = 21,000")
elif TRE and sem3 and P50 and Sci:
    print ("Registration fee = 4,500")
elif TRE and sem3 and P56 and Sci:
    print ("Registration fee = 5,250")
elif Bundit and sem1 and P50 and Sci:
    print ("Registration fee = 26,000")
elif Bundit and sem1 and P56 and Sci:
    print ("Registration fee = 31,000")
elif Bundit and sem3 and P50 and Sci:
    print ("Registration fee = 7,000")
elif Bundit and sem3 and P56 and Sci:
    print ("Registration fee = 7,750")
elif not(sem1 or sem3):
    print ("INVALID SEMESTER")
else:
    print ("INVALID  ID")
