QQQ=int(input("請輸入一個正整數(<10):"))
WWW=str("")
EEE=int(0)
if(QQQ<=10):
    for i in range(1,QQQ+1):
        for o in range(1,i+1):
            EEE=i*o
            if(EEE>=100):
                WWW=WWW+" "
            WWW=WWW+("%3d"%EEE)
        print(WWW)
        WWW=""

    
