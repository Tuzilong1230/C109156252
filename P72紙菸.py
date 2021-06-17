QQQ =int(input("請輸入n:"))
WWW =int(input("請輸入k:"))
EEE =int(0)
RRR =int(QQQ)
TTT =int(0)
while(QQQ//WWW>=1):
    QQQ =RRR
    EEE +=QQQ
    RRR =(QQQ+TTT) // WWW
    TTT =QQQ %  WWW
    
print("Peter可以抽",EEE,"支紙菸")
