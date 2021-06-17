
WWW = str("1234")
AAA= int(0)
BBB= int(0)
while(AAA != 4):
    QQQ = str(input(":"))

    for i in range(0,4):
        if QQQ[i]==WWW[i]:
            AAA=AAA+1
        elif QQQ[i] in WWW:
            BBB=BBB+1
    print(str(AAA),"A",str(BBB),"B")
    AAA= int(0)
    BBB= int(0)
print("")

    
    
