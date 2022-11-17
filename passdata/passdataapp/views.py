from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def dice(request):
  # return HttpResponse("Hello Django!")
  number = random.randint(1, 6)
  return render(request, "dice.html", {"no": number})

def dice2(request):
  number1 = random.randint(1, 6)
  number2 = random.randint(1, 6)
  number3 = random.randint(1, 6)
  return render(request, "dice2.html", {"no1": number1, "no2": number2, "no3": number3})
  
def dice3(request):
  # times = 0
  # times = times + 1
  # local_times = times
  username = "Django"
  dict_no = {"no": random.randint(1, 6)}
  return render(request, "dice3.html", locals())

def show(request):
  # list = range(1, 6)
  # 還沒講到資料庫，先使用此方式
  person1 = {"name":"Amy", "phone":"02-222111444", "age":20}
  person2 = {"name":"Jack", "phone":"02-777111444", "age":21}
  person3 = {"name":"Nacy", "phone":"09-223111444", "age":33}
  persons = [person1, person2, person3]
  return render(request, "show.html", locals())
