from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def hello_world(request):
    return render(request, 'layui.html', {})
    
def table(request):
    return render(request, 'table.html', {})  


def json(request):
    from os.path import dirname
    t = os.path.abspath(os.path.dirname(__file__))
    tt = dirname(t)
    f = os.path.abspath(os.path.dirname(__file__))
    print(f)
    #file_path = BASE_DIR + '/json
    f = open(tt + '/json/table/demo1.json', 'r', encoding="utf8")
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="application/json")    
    #return HttpResponse(file_content, content_type="text/plain")    
    
def json2(request):
    #print(BASE_DIR)
    f = os.path.abspath(os.path.dirname(__file__))
    #print(f)
    #file_path = BASE_DIR + '/json
    from os.path import dirname
    t = os.path.abspath(os.path.dirname(__file__))
    tt = dirname(t)    
    f = open(tt + '/json/table/demo2.json', 'r', encoding="utf8")
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="application/json")    
    #return HttpResponse(file_content, content_type="text/plain")    

def admintest(request):
    return render(request, 'admin.html', {})
    
def all(request):
    return render(request, 'all.html', {})    
    
def button(request):
    return render(request, 'button.html', {})    
    
def form(request):
    return render(request, 'form.html', {})    

def xingzuo(request):
    return render(request, 'xingzuo.html', {})    
    
    
    
