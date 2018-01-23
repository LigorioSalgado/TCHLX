from django.shortcuts import render,get_object_or_404
from .models import Post,Categories
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    imagen = "/static/img/sidebar.jpg"
    posts_list =  Post.objects.filter(publicado=True).select_related('autor').order_by('-fecha_publicacion')
    categories = Categories.objects.all()
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page',1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)



    return render(request,'blog/index.html',{'image':imagen,'posts':posts, 'categories':categories})



def post(request,slug):

    post = get_object_or_404(Post,slug=slug)
    print('post: '+post.titulo)
    related = Post.objects.filter(Q(categoria=post.categoria) | Q(autor=post.autor), ~Q(titulo=post.titulo))[:3]
    return render(request,'blog/post/post.html',{'post':post,'related':related})