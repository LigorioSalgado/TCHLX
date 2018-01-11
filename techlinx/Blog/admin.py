from django.contrib import admin
from .models import Post,Categories
from techlinx.Staff.models import Staff
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ('titulo','contenido','cover',
    'categoria','publicado')
    
    def get_form(self, request, *args, **kwargs):
        form = super(PostAdmin, self).get_form(request, *args, **kwargs)
        autor = Staff.objects.get(user=request.user)
        form.base_fields['autor'].initial = autor
        form.request = request
        return form

class CategorieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Categories,CategorieAdmin)