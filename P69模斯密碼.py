QQQ = {"-----":0,".----":1,"..---":2,"...--":3,"....-":4,".....":5,"-....":6,"--...":7,"---..":8,"----.":9}
WWW = str(input("輸入摩斯密碼:"))
RRR=str("")
EEE=str("")
YYY=int(0)
arr=[]
for i in range(0,len(WWW)):
    YYY=YYY+1
    TTT=WWW[i]
    EEE=EEE+str(TTT)
    if((YYY%5==0) and i!=0):
        RRR=RRR+str(QQQ[EEE])
        EEE=str("")
print(RRR)
        
        
