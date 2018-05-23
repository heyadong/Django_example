from django.urls import path
from .views import book,book_detail,login
# 应用命名空间，在urls.py 文件中定义app_name变量：在进行url反转时可以使用reverse(appname:url_name)
app_name = 'book'
urlpatterns = [
    path('',book),
    path('detail/<int:id>',book_detail),
    path('login',login,name='login')
]