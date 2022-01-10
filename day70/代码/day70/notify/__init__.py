import settings
import importlib


def send_all(content):
    for path_str in settings.NOTIFY_LIST:  #'notify.email.Email'
        module_path,class_name = path_str.rsplit('.',maxsplit=1)
        # module_path = 'notify.email'  class_name = 'Email'
        # 1 利用字符串导入模块
        module = importlib.import_module(module_path)  # from notify import email
        # 2 利用反射获取类名
        cls = getattr(module,class_name)  # Email、QQ、Wechat
        # 3 生成类的对象
        obj = cls()
        # 4 利用鸭子类型直接调用send方法
        obj.send(content)
