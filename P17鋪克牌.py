QQ =str(input(":"))
QQQ =QQ.split(" ")
EEE = int(0)
WWW = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
for i in range(0,5):
    EEE = int(WWW[QQQ[i]])+EEE
print(str(EEE))
