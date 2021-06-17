AAA={}


QQQ=int(input("輸入n值:"))
for i in range(0,QQQ):
    WWW=str(input("請輸入姓名:"))
    EEE=str(input("請輸入電子郵件:"))
    AAA[WWW]=EEE
    
RRR=str(input("請輸入要查詢電子郵件的姓名:"))
print(RRR,"電子郵件帳號為",AAA[RRR])
