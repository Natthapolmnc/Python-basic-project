ID=input()
Semes=int(input())
if (ID[:2]=="60" or ID[:2]=="59" or ID[:2]=="58" or ID[:2]=="57" or ID[:2]=="56" or ID[:2]=="61" and ID[8:] =="23" and Semes<=2 and ID[2]== "7"):
    print ("Registration fee = 31000")
elif (ID[:2]=="60" or ID[:2]=="59" or ID[:2]=="58" or ID[:2]=="57" or ID[:2]=="56" or ID[:2]=="61" and ID[8:] =="23" and Semes<=2 and ID[2] != "7"):
    print("Registration fee = 21000")
elif (ID[:2]=="60" or ID[:2]=="59" or ID[:2]=="58" or ID[:2]=="57" or ID[:2]=="56" or ID[:2]=="61" and ID[8:] =="23" and Semes==3 and ID[2] == "7"):
    print("Registration fee = 5250")
elif (ID[:2]=="60" or ID[:2]=="59" or ID[:2]=="58" or ID[:2]=="57" or ID[:2]=="56" or ID[:2]=="61" and ID[8:] =="23" and Semes==3 and ID[2] != "7"):
    print ("Registration fee = 7750")
elif (ID[:2]=="55" or ID[:2]=="54" or ID[:2]=="53" or ID[:2]=="52" or ID[:2]=="51" or ID[:2]=="50" and ID[8:] =="23" and Semes<=2 and ID[2] == "7"):
    print ("Registration fee = 26000")
elif (ID[:2]=="55" or ID[:2]=="54" or ID[:2]=="53" or ID[:2]=="52" or ID[:2]=="51" or ID[:2]=="50" and ID[8:] =="23" and Semes<=2 and ID[2] != "7"):
    print ("Registration fee = 18000")
elif (ID[:2]=="55" or ID[:2]=="54" or ID[:2]=="53" or ID[:2]=="52" or ID[:2]=="51" or ID[:2]=="50" and ID[8:] =="23" and Semes==3 and ID[2] == "7"):
    print ("Registration fee = 7000")
elif (ID[:2]=="55" or ID[:2]=="54" or ID[:2]=="53" or ID[:2]=="52" or ID[:2]=="51" or ID[:2]=="50" and ID[8:] =="23" and Semes==3 and ID[2] != "7"):
    print ("Registration fee = 4500")   
else: 
    print ("Invalid ID")