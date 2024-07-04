#そのまま文字列として出力
answer= '''○●●●
●○●●
●●○●
●●●○
'''
print(answer)

#制御文字と掛け算を使用
w= "○"
b= "●"
answer_1= w + b*3 + "\n" + b + w + b*2 + "\n" + b*2 + w + b + "\n" + b*3 + w
print(answer_1)
