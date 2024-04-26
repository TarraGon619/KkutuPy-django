from django.shortcuts import render

# Create your views here.
def lobby(req):
    return render(req, "main/lobby.html")