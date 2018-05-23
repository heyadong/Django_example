### Django url 反转/重定向 reverse/redirect
函数反转： reverse 可传递关键字参数（**kwargs)
   '''
    1.如果在反转url时需要添加参数：可传入关键字参数格式如下：
     reverse('detail/',kwargs={'detail_id'：1，'page':2}
    2.如果是查询字符串使用拼接
     reverse('detail/')+'?name=1'
   ''

from django.shortcut import reverse,redirect
eg:
def login(request):
    if request.GET.get('name',None) is None:
    return redirect(reverse('book:signup'))


def signup(request):
    return HttpResponse('请注册')


### path/re_path
urls.py 文件：
1.url 命名
2.应用命名空间： 在urls.py 中使用app_name ='book' 在url 翻转是可以使用：reverse('app_name:login')

app_name ='book'
urlpatterns = [
   path('signup/', signup,name='signup')  # path 中可传入参数name 给url命名，反转可以使用
   re_path(r'^book/(?P<id>\d{4})/$',login) # re_path 让url支持正则表达式，只接受指定规则的URL
]

