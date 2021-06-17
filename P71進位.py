QQQ =int(input("請輸入十進位的正整數:"))
WWW =int(input("請輸入進位:"))
EEE=int(1)
RRR=str("")
AAA=int(0)
SSS=int(0)
while(EEE==1):
    AAA=QQQ//WWW
    SSS=int(QQQ%WWW)
    RRR=str(SSS)+RRR
    QQQ=AAA
    print(QQQ)
    if(QQQ<WWW):
        break
RRR=str(AAA)+RRR
print(RRR)
    
    
    
    
