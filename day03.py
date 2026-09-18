import random
print("欢迎来到猜数字游戏！我已经选择了一个1到100之间的数字。")
target = random.randint(1, 100)
guess = 0
while guess != target:
    guess = int(input("请输入你的猜测:"))
    if guess < target:
        print("太小了！")
    elif guess > target:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")