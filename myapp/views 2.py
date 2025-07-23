from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    content="<html><body><h1>Welcome to My Django App</h1></body></html>"
    return HttpResponse(content)

def hello(request):
    content="<html><body><h1>Hello, world! This is my first Django app.</h1></body></html>"
    return HttpResponse(content)

def display_time(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 


def index(request): 
    path = request.path 
    method = request.method 
    schema = request.scheme
    host = request.get_host()
    adress = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    reponse =HttpResponse()
    reponse.headers['Age']=20


    content=f''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {path}</p> 
<p>Request Method :{method}</p>
<p>Request Scheme :{schema}</p>
<p>Request Host :{host}</p>
<p>Request Address :{adress}</p>
<p>Request User-Agent :{user_agent}</p>
<p>Request Path Info :{path_info}</p>
<p>Response Age :{reponse.headers}</p>

</center> 
'''
    return HttpResponse(content,content_type='text/html',charset='utf-8') 

def menuitems(request, dish):
    items = { 
        'pasta': "Pasta with tomato sauce",
        'pizza': "Pizza with cheese and pepperoni",
        'salad': "Fresh garden salad",
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2> "+description)

