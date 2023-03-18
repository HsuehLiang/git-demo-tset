import random

x = random.randint(1, 50)
print(x)

win = False
start, end = 1, 50
for i in range(5):
    y = eval(input(f'猜 {start} ~ {end} 之間的數字:'))
    if x == y:
        win = True
        break
    if x > y:
        if start < y:
            start = y
    else:
        if end > y:
            end = y
if win:
    print(f'猜中了！你猜了{i+1}次')
else:
    print(f'沒猜中，遊戲結束了! 正確答案為：{x}')
