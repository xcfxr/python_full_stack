while True:
    msg = """
    0 退出
    1 登录
    2 注册
    """
    print(msg)
    cmd = input('请输入命令编号>>: ').strip()
    if not cmd.isdigit():
        print('必须输入命令编号的数字，傻叉')
        continue

    if cmd == '0':
        break
    elif cmd == '1':
        # 登录功能代码（附加：可以把之前的循环嵌套，三次输错退出引入过来）
        pass
    elif cmd == '2':
        # 注册功能代码
        pass
    else:
        print('输入的命令不存在')