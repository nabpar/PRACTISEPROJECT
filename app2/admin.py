from django.contrib import admin
from .models import Topic
# Register your models here.




class TopicAdmin(admin.ModelAdmin):
    list_display  = ['id','name','category','subject','date_created','date_updated']

admin.site.register(Topic,TopicAdmin)
