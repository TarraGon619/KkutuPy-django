from django.shortcuts import render

# Create your views here.
def logIn(req):
    return render(req, "login/login.html")

def signIn(req):
    return render(req, 'login/signin.html')