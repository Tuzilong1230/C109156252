QQQ = int(input("組數:"))
EEE = list()
RRR = list()
TTT = int(0)
for i in range(1,QQQ+1):
    WWW =str(input("第%d組:"%i))
    EEE = WWW.split(" ")
    RRR.append(EEE)
for i in range(0,QQQ):
    TTT = 0
    TTT = int(RRR[i][0])*250+TTT
    TTT = int(RRR[i][1])*175+TTT
    print("第%d組"%i,str(TTT))
