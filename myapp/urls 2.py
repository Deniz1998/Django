# myapp/urls.py
from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('hello/', views.hello, name='hello'),
    path('time/', views.display_time, name='display_time'),
    path('', views.index, name='index'),
    path('pathview/<str:name>/<int:id>/', views.pathview, name='pathview'),  
    # path('qryview/', views.qryview, name='qryview'),  #http://127.0.0.1:8000/myapp/qryview/?name=John&id=42
    path('dishes/<str:dish>', views.menuitems, name='menuitems'),
    re_path(r'^menu_item/([0-9]{2})/$',views.menuitems, name='menu_item'),
]

