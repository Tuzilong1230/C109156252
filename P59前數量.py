QQQ=str(int(input("輸入金額:")))
WWW=int(QQQ[0])
QQQ1=int(QQQ[1])
QQQ2=int(QQQ[2])
if(QQQ1>=5):
    WWW=QQQ1+WWW-4
else:
    WWW=WWW+QQQ1
if(QQQ2>=5):
    WWW=WWW+QQQ2-4
else:
    WWW=WWW+QQQ2
print(WWW)
    
