from django.shortcuts import render,HttpResponse,redirect
from app01.myforms import MyRegForm
from app01 import models
from django.http import JsonResponse
# Create your views here.


def register(request):
    form_obj = MyRegForm()
    if request.method == 'POST':
        back_dic = {"code": 1000, 'msg': ''}
        # 校验数据是否合法
        form_obj = MyRegForm(request.POST)
        # 判断数据是否合法
        if form_obj.is_valid():
            # print(form_obj.cleaned_data)  # {'username': 'jason', 'password': '123', 'confirm_password': '123', 'email': '123@qq.com'}
            clean_data = form_obj.cleaned_data  # 将校验通过的数据字典赋值给一个变量
            # 将字典里面的confirm_password键值对删除
            clean_data.pop('confirm_password')  # {'username': 'jason', 'password': '123', 'email': '123@qq.com'}
            # 用户头像
            file_obj = request.FILES.get('avatar')
            """针对用户头像一定要判断是否传值 不能直接添加到字典里面去"""
            if file_obj:
                clean_data['avatar'] = file_obj
            # 直接操作数据库保存数据
            models.UserInfo.objects.create_user(**clean_data)
            back_dic['url'] = '/login/'
        else:
            back_dic['code'] = 2000
            back_dic['msg'] = form_obj.errors
        return JsonResponse(back_dic)
    return render(request,'register.html',locals())


def login(request):
    return render(request,'login.html')

"""
图片相关的模块
    pip3 install pillow
"""
from PIL import Image,ImageDraw,ImageFont
"""
Image:生成图片
ImageDraw:能够在图片上乱涂乱画
ImageFont:控制字体样式
"""
from io import BytesIO,StringIO
"""
内存管理器模块
BytesIO:临时帮你存储数据 返回的时候数据是二进制
StringIO:临时帮你存储数据 返回的时候数据是字符串
"""
import random
def get_random():
    return random.randint(0,255),random.randint(0,255),random.randint(0,255)
def get_code(request):
    # 推导步骤1:直接获取后端现成的图片二进制数据发送给前端
    # with open(r'static/img/111.jpg','rb') as f:
    #     data = f.read()
    # return HttpResponse(data)

    # 推导步骤2:利用pillow模块动态产生图片
    # img_obj = Image.new('RGB',(430,35),'green')
    # img_obj = Image.new('RGB',(430,35),get_random())
    # # 先将图片对象保存起来
    # with open('xxx.png','wb') as f:
    #     img_obj.save(f,'png')
    # # 再将图片对象读取出来
    # with open('xxx.png','rb') as f:
    #     data = f.read()
    # return HttpResponse(data)

    # 推导步骤3:文件存储繁琐IO操作效率低  借助于内存管理器模块
    # img_obj = Image.new('RGB', (430, 35), get_random())
    # io_obj = BytesIO()  # 生成一个内存管理器对象  你可以看成是文件句柄
    # img_obj.save(io_obj,'png')
    # return HttpResponse(io_obj.getvalue())  # 从内存管理器中读取二进制的图片数据返回给前端


    # 最终步骤4:写图片验证码
    img_obj = Image.new('RGB', (430, 35), get_random())
    img_draw = ImageDraw.Draw(img_obj)  # 产生一个画笔对象
    img_font = ImageFont.truetype('static/font/222.ttf',30)  # 字体样式 大小

    # 随机验证码  五位数的随机验证码  数字 小写字母 大写字母
    code = ''
    for i in range(5):
        random_upper = chr(random.randint(65,90))
        random_lower = chr(random.randint(97,122))
        random_int = str(random.randint(0,9))
        # 从上面三个里面随机选择一个
        tmp = random.choice([random_lower,random_upper,random_int])
        # 将产生的随机字符串写入到图片上
        """
        为什么一个个写而不是生成好了之后再写
        因为一个个写能够控制每个字体的间隙 而生成好之后再写的话
        间隙就没法控制了
        """
        img_draw.text((i*60+60,-2),tmp,get_random(),img_font)
        # 拼接随机字符串
        code += tmp
    print(code)
    # 随机验证码在登陆的视图函数里面需要用到 要比对 所以要找地方存起来并且其他视图函数也能拿到
    request.session['code'] = code
    io_obj = BytesIO()
    img_obj.save(io_obj,'png')
    return HttpResponse(io_obj.getvalue())





