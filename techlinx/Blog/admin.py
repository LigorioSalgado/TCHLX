from django.contrib import admin
from .models import Post, Categories
from techlinx.Staff.models import Staff
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summer_note_fields = ('contenido',)
    fields = ('titulo','contenido','cover','categoria','publicado')
    readonly_fields = ('time_estimate',)
   
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        try:
            editor = Staff.objects.filter(user=request.user,editor=True).exists()
        except Exception  as e:
            print("Excepcion "+ str(e))
            editor = False
        print(editor)
        if request.user.is_superuser or editor:
            return qs
        return qs.filter(autor__user=request.user)

    def save_model(self, request, obj, form, change):
        print("Cambios??? "+ str(change))
        if not change:
            obj.autor = Staff.objects.get(user__id=request.user.id)
        super().save_model(request, obj, form, change)

    def author(self, instance):
        return instance.autor

    def time_estimate(self, instance):
        return instance.tiempo_estimados

    author.short_description = "Autor del post"
    time_estimate.short_description = "Tiempo estimado de lectura"

    

class CategorieAdmin(admin.ModelAdmin):
    fields = ('nombre','imagen')


admin.site.register(Post, PostAdmin)
admin.site.register(Categories, CategorieAdmin)
