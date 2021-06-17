
WWW=int(0)
EEE=int(0)


RRR=str(input("請輸入第一組數字:"))
TTT=str(input("請輸入第二組數字:"))
for i in range(0,len(RRR)):
    if(RRR[i]==TTT[i]):
        WWW=WWW+1
AAA=set(RRR)
SSS=set(TTT)
for o in AAA:
    if(o in SSS):
        EEE=EEE+1
EEE=EEE-WWW
if(EEE!=0):
    print(WWW,"A",EEE,"B 加油")
else:
    print(WWW,"A",EEE,"B 全對")

