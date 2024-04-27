from django.shortcuts import render

# Create your views here.
def lobby(req):
    title = "장고님의 방"
    return render(req, "main/lobby.html", {'title':title})

def room(req):
    return render(req, "main/room.html")