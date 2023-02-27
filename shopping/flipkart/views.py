from django.shortcuts import render,redirect
from .models import signup
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password,make_password

def index(request):
    return render(request,'home.html')
def signup(request):
    if request.method=="POST":
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        email_id=request.POST.get('email')
        password=request.POST.get('pwd')
        mobile=request.POST.get('mbl')
        gender=request.POST.get('gender')

        save_info=signup(firstname=first_name,lastname=last_name,email=email_id,password=make_password(password),mobile=mobile,gender=gender)
        save_info.save()
        return HttpResponse("success")

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            fetchObj=signup.object.get(email=email)
            if check_password(password,fetchObj.password):
                request.session['name']=fetchObj.firstname
                return redirect('contact')
            else:
                return HttpResponse('wrong password')
        except:
                return HttpResponse('wrong email')