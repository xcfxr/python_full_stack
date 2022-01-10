from django.shortcuts import render,HttpResponse

# Create your views here.
import json
from django.http import JsonResponse

def ab_ajax(request):
    if request.method == "POST":
        # print(request.POST)  # <QueryDict: {'username': ['jason'], 'password': ['123']}>
        # i1 = request.POST.get('i1')
        # i2 = request.POST.get('i2')
        # 先转成整型再加
        # i3 = int(i1) + int(i2)
        # print(i3)
        # d = {'code':100,'msg':i3}
        d = {'code':100,'msg':666}
        return HttpResponse(json.dumps(d))
        # return JsonResponse(d)
    return render(request,'index.html')