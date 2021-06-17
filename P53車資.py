QQQ=float(input("請輸入公里數(km):"))
MMM=int(0)
AAA=int(0)
SSS=int(0)
if(QQQ>1.5):
    QQQ=QQQ-1.5
    AAA=QQQ//0.25
    SSS=QQQ%0.25
    if(SSS!=0):
        AAA=AAA+1
MMM=AAA*5+75
print("所需車資:",int(MMM),"元")
    
