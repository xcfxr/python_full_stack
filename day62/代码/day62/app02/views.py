from django.shortcuts import render,HttpResponse,reverse

# Create your views here.


def reg(request):
    # print(reverse('reg'))
    # print(reverse('app02:reg'))
    print(reverse('app02_reg'))
    return HttpResponse('app02 reg')
