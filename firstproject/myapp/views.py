from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def sayhello(request):
  return HttpResponse("Hello Django!")

def hello2(request, username):
  now = datetime.now()
  return render(request, "hello3.html", locals())

def hello4(request, username):
  now = datetime.now()
  return render(request, "hello4.html", locals())