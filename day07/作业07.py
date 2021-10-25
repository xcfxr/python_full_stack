count = 0
res = 17
while count < 3:
    age = input('请输入猜测的年龄：')

    if age.isdigit():
        age = int(age)
        if age == res:
            print('猜对啦，恭喜！')
            break
        elif age < res:
            print('猜小啦')
        else:
            print('猜大了')
    else:
        print('请输入数字')
    count += 1