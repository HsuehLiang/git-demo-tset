import random

x = random.randint(1, 50)
print(x)

win = False
for i in range(5):
    y = eval(input('猜一數字(1~50:)'))
    if x == y:
        win = True
        break
    if x > y:
        print('猜大一點')
    else:
        print('猜小一點')

if win:
    print(f'恭喜過關！你總共猜了{i+1}次')
else:
    print(f'遊戲結束!答案為：{x}')
