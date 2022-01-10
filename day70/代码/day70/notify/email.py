class Email(object):
    def __init__(self):
        pass  # 发送邮箱需要做的前期准备工作

    def send(self, content):
        print('邮箱通知:%s' % content)