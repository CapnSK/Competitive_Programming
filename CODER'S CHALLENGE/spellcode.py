bob=['tie','tei','eti','eit','iet','ite']
for _ in range(int(input())):
    vals1=input()
    vals2=input()
    if(vals1[0]+vals1[1]+vals1[2] in bob):
        print('yes')
    elif(vals1[0]+vals1[1]+vals2[2] in bob):
        print('yes')
    elif(vals1[0]+vals2[1]+vals1[2] in bob):
        print('yes')
    elif(vals1[0]+vals2[1]+vals2[2] in bob):
        print('yes')    
    elif(vals2[0]+vals1[1]+vals1[2] in bob):
        print('yes')
    elif(vals2[0]+vals1[1]+vals2[2] in bob):
        print('yes')
    elif(vals2[0]+vals2[1]+vals1[2] in bob):
        print('yes')    
    elif(vals2[0]+vals2[1]+vals2[2] in bob):
        print('yes')
    else:
        print('no')