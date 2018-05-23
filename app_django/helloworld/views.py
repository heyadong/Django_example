from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
# 试图函数参数;request
def book(request):
    if request.GET.get('name') is None:
        return redirect(reverse('book:login'))
    return HttpResponse("这是图书首页")

def book_detail(request,id):
    kind = request.GET.get('kind','kinds') # 或者request.GET.get('kind')
    book = "book's id is %s, the kind of book is %s" %(id, kind)
    return HttpResponse(book)
def login(request):
    return HttpResponse('这是登陆页面')