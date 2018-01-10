from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

def path_save_images(instance,filname):
    return "{0}/{1}".format(instance.slug,filname)

class Staff(models.Model):
    id = models.UUIDField(primary_key = True,
        unique = True,
        editable = False,
        default = uuid.uuid4 )
    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        related_name = "usuario"
    )
    slug = models.SlugField(max_length=180, 
        unique = True)
    biografia = models.TextField(help_text="Biografia del miembro del Staff")
    imagen = models.ImageField(
        max_length = models.ImageField(upload_to=path_save_images,
        help_text="Imagen del miembro del staff")
    )
    autor = models.BooleanField(verbose_name="¿Es autor?",
        default = False,
        help_text = "Marcar si es autor")
    editor = models.BooleanField(verbose_name="¿Es Editor?",
        default = False,
        help_text = "Marcar si es Editor")
    facebook = models.URLField(verbose_name="Perfil de Facebook",
        help_text = "URL del Perfil de Facebook", 
        null = True,
        blank = True )
    twitter = models.URLField(verbose_name="Perfil de Twitter",
        help_text = "URL del Perfil de Twitter", 
        null = True,
        blank = True )
    GitHub = models.URLField(verbose_name="Perfil de GitHub",
        help_text = "URL del Perfil de GitHub", 
        null = True,
        blank = True) 
    pagina_personal = models.URLField(verbose_name="Pagina personal",
        help_text = "URL del Perfil de pagina personal", 
        null = True,
        blank = True)
    posts = models.ManyToManyField(
        'techlinx.Blog.models.Post',
        related_name="publicaciones"
    )
    
    






   
