from django.contrib import admin
from .models import PRG
# Register your models here.


class PRGAdmin(admin.ModelAdmin):
    list_display = ['id','title','name','image','tags',]

admin.site.register(PRG,PRGAdmin)
