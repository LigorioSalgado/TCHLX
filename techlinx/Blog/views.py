from django.shortcuts import render,get_object_or_404
from .models import Post,Categories
# Create your views here.


def index(request):
    imagen = "/static/img/default-sidebar.jpg"
    posts =  Post.objects.filter(publicado=True).select_related('autor').order_by('-fecha_publicacion')
    categories = Categories.objects.all()
    print(posts.count())

    return render(request,'blog/index.html',{'image':imagen,'posts':posts, 'categories':categories})



def post(request,slug):

    post = get_object_or_404(Post,slug=slug)
    print('post: '+post.titulo)
    return render(request,'blog/post/post.html',{'post':post})