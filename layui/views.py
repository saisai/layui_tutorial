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

def jsons(request):
    return HttpResponse('json/demo1.json')
    #return render(request, 'json/demo1.json', {})   

def json(request):
    print(BASE_DIR)
    f = os.path.abspath(os.path.dirname(__file__))
    print(f)
    #file_path = BASE_DIR + '/json
    f = open(f + '/json/table/demo1.json', 'r', encoding="utf8")
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="application/json")    
    #return HttpResponse(file_content, content_type="text/plain")    
    
