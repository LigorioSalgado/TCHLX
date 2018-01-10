from django.shortcuts import render

# Create your views here.


def index(request):
    imagen = "/static/img/default-sidebar.jpg"
    return render(request,'blog/index.html',{'image':imagen})