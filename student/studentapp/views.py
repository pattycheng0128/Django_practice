from django.shortcuts import render
from studentapp.models import student

# Create your views here.
def listone(request):
  unit = student.objects.get(cName="Lulu") #讀取一筆資料
  return render(request, "listone.html", locals())

def listall(request):
  students = student.objects.all().order_by('id')
  return render(request, "listall.html", locals())