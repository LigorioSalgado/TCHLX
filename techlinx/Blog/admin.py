from django.contrib import admin
from .models import Post,Categories
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

class CategorieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Categories,CategorieAdmin)