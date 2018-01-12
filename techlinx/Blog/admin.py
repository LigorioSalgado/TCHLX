from django.contrib import admin
from .models import Post, Categories
from techlinx.Staff.models import Staff
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    fields = ('titulo','contenido','cover','categoria','publicado','time_estimate')
   
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        print(request.user.usuario.editor)
        if request.user.is_superuser or request.user.usuario.editor:
            return qs
        return qs.filter(autor__user=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = Staff.objects.get(user__id=request.user.id)
        super().save_model(request, obj, form, change)

    def author(self, instance):
        return instance.autor

    def time_estimate(self, instance):
        return instance.tiempo_estimado
    author.short_description = "Autor del post"
    time_estimate.short_description = "Tiempo estimado de lectura"


class CategorieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Categories, CategorieAdmin)
