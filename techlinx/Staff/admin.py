from django.contrib import admin
from .models import Staff
# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    exclude = ('slug', )

admin.site.register(Staff,StaffAdmin)