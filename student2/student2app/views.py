from django.shortcuts import render, redirect
from student2app.models import student

# Create your views here.
def post(request):
  if request.method == "POST":
    mess = request.POST['username']
  else:
    mess = "表單資料尚未送出!"
  return render(request, "post.html", locals())

def post1(request):
  if request.method == "POST":
    cName = request.POST['cName']
    cSex = request.POST['cSex']
    cBirthday = request.POST['cBirthday']
    cEmail = request.POST['cEmail']
    cPhone = request.POST['cPhone']
    cAddr = request.POST['cAddr']
    # 新增一筆資料
    unit = student.objects.create(cName=cName, cSex=cSex,cBirthday=cBirthday, cEmail=cEmail,
            cPhone=cPhone, cAddr=cAddr)
    unit.save() #寫入資料庫
    return redirect('/index/')
  else:
    message = "請輸入資料(資料不做驗證)"
  return render(request, "post1.html", locals())
