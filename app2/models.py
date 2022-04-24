from django.db import models

# Create your models here.






class Topic(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 100)
    category = models.CharField(max_length= 100)
    subject = models.CharField( max_length=50)
    date_created = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateTimeField(auto_now= True) 

