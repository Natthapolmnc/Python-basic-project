dic={2301117:['Calculus I',4],2301118:['Calculus II',4],2301286:['Probability and Statistics',3],2301399:['Project Proposal',1],2301499:['Senior Project',2],2302113:['General Chemistry Lab I',1],2302161:['General Chemistry',3]}
ci=int(input('Course ID : '))
while ci!=0:
    if ci in dic:
        print(dic[ci][0],dic[ci][1])
    else:
        print ('Unknown')
    ci=int(input('Course ID : '))