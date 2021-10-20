count = 0
res = 17
while count < 3:
    age = input('请输入猜测的年龄：')
    age = int(age)
    if age == res:
        print('猜对啦，恭喜！')
        break
    elif age < res:
        print('猜小啦')
    else:
        print('猜大了')
    count += 1