QQQ =str("鼠、牛、虎、兔、龍、蛇、馬、羊、猴、雞、狗、豬")
QQQ1 = QQQ.split("、")
print(str(QQQ1))
WWW = int(input(":"))
WWW1 = WWW-1911
print(QQQ1[(WWW1-1)%12])
