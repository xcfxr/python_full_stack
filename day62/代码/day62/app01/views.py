from django.shortcuts import render,redirect,HttpResponse,reverse

# Create your views here.


def index(request):
    # return HttpResponse('')  # 符合
    # return render(request,'home.html')  # 符合
    """
    def render(request, template_name, context=None, content_type=None, status=None, using=None):
        content = loader.render_to_string(template_name, context, request, using=using)
        return HttpResponse(content, content_type, status)
    """
    # return redirect()  # 符合

    from django.template import Template,Context
    res = Template('<h1>{{ user }}</h1>')
    con = Context({'user':{'username':'jason','password':123}})
    ret = res.render(con)
    print(ret)
    return HttpResponse(ret)


def func(request,year):
    return HttpResponse('func')


def home(request):
    # print(reverse('xxx', args=(1,)))  # /index/1/
    # 有名分组反向解析 写法1
    # print(reverse('ooo',kwargs={'year':123}))
    # 简便的写法
    print(reverse('ooo',args=(111,)))
    return render(request, 'home.html')


def reg(request):
    # print(reverse('reg'))
    # 名称空间解析
    # print(reverse('app01:reg'))
    print(reverse('app01_reg'))
    return HttpResponse('app01:reg')


import json
from django.http import JsonResponse
def ab_json(request):
    user_dict = {'username':'jason好帅哦,我好喜欢!','password':'123','hobby':'girl'}

    l = [111,222,333,444,555]
    # 先转成json格式字符串
    # json_str = json.dumps(user_dict,ensure_ascii=False)
    # 将该字符串返回
    # return HttpResponse(json_str)
    # 读源码掌握用法
    # return JsonResponse(user_dict,json_dumps_params={'ensure_ascii':False})
    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    # return JsonResponse(l,safe=False)



def ab_file(request):
    if request.method == 'POST':
        print(request.body)  # 原生的浏览器发过来的二进制数据
        # print(request.POST)  # 只能获取普通的简直对数据 文件不行
        # print(request.FILES)  # 获取文件数据
        # <MultiValueDict: {'file': [<InMemoryUploadedFile: u=1288812541,1979816195&fm=26&gp=0.jpg (image/jpeg)>]}>
        # file_obj = request.FILES.get('file')  # 文件对象
        # print(file_obj.name)
        # with open(file_obj.name,'wb') as f:
        #     for line in file_obj.chunks():  # 推荐加上chunks方法 其实跟不加是一样的都是一行行的读取
        #         f.write(line)

    print(request.path)  # /app01/ab_file/
    print(request.path_info)  # /app01/ab_file/
    print(request.get_full_path())  # /app01/ab_file/?username=jason

    return render(request,'form.html')


from django.views import View


class MyLogin(View):
    def get(self,request):
        return render(request,'form.html')

    def post(self,request):
        return HttpResponse('post方法')








