Q1 = str("春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。")
Q2 = str("紅豆生南國，春來發幾支?願君多採擷，此物最相思。")
QQ1 = list()
QQ2 = list()
for i in Q1:
    if(i!="，"and i!="。"):
        QQ1.append(i)
for i in Q2:
    if (i in QQ1):
        QQ2.append(i)
print(QQ2)
