QQQ=str(input("輸入M個正整數:"))
WWW=[]
AAA=int(0)
SSS=int(0)
DDD=[]
EEE=str("")
for i in range(0,len(QQQ)):
    if(QQQ[i]!=","):
        EEE=EEE+QQQ[i]
    else:
        WWW.append(EEE)
        EEE=""
WWW.append(EEE)
#print(WWW)
for i in range(0,len(WWW)):
    for o in range(0,len(WWW)):
        if(i!=o):
            AAA=int(WWW[i])
            SSS=int(WWW[o])
            #print(AAA,SSS)
            for p in range(1,AAA):
                if(SSS%p==0):
                    DDD.append(p)
                    #print(p)
print(max(DDD))
                    
            
    
