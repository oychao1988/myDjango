import json

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('weweb index')

def get_params_from_url_regex(request, a, b):
    return HttpResponse('get_params_from_url_regex<br>a: %s<br>b: %s' % (a, b))

def get_params_from_url_name(request, a, b):
    return HttpResponse('get_params_from_url_name<br>a: %s<br>b: %s' % (a, b))

def get_params_from_request(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    return HttpResponse('get_params_from_request<br>a: %s<br>b: %s' % (a, b))

def get_params_from_form(request):
    print(request.POST)
    a = request.POST.get('a')
    b = request.POST.get('b')

    # print(request.body)
    # json_data = request.body.decode()
    # dict_data = json.loads(json_data)
    #
    # print(dict_data)
    # a = dict_data.get('a')
    # b = dict_data.get('b')
    return HttpResponse('get_params_from_form<br>a: %s<br>b: %s' % (a, b))


def set_cookie(request):
    response = HttpResponse(content = 'set cookie success')
    response.set_cookie('name', 'cino', max_age=3600)
    response.set_cookie('gender', 'female', max_age=3600)
    response.set_cookie('age', '18', max_age=3600)
    # response.content = 'set cookie success'
    return response

def get_cookie(request):
    response = HttpResponse()
    name = request.COOKIES.get('name')
    gender = request.COOKIES.get('gender')
    age = request.COOKIES.get('age')
    response.content = 'name: %s<br>gender: %s<br>age: %s' % (name, gender, age)
    return response