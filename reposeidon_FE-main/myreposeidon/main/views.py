from django.shortcuts import render

# Create your views here.
def sign_up(request):
    return render(request,"signup.html")

def after_sign_up(request):
    return render(request,"main_afterLogin.html")

def before_login(request):
    return render(request,"main_beforeLogin.html") 