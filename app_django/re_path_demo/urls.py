from django.urls import path,re_path
from .views import index
app_name = 'repath'
urlpatterns = [
    re_path(r'^(?P<name>\d{4})/$', index)
]
