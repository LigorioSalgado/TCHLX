from django.contrib import admin
from .models import Staff
# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(Staff,StaffAdmin)