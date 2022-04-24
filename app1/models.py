from django.db import models
from PROJECT.utils import unique_slug_generator
from django.db.models.signals import pre_save 
from django.dispatch import receiver
from taggit.managers import TaggableManager
# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)




class PRG(models.Model):
  title = models.CharField(max_length=200,null=True)
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to= upload_to)
  slug = models.SlugField(unique=True,null=True,blank=True)
  tags = TaggableManager()




def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
       instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender= PRG)


# @receiver(pre_save, sender=PRG)
# def pre_save_receiver(sender, instance, *args, **kwargs):
#    if not instance.slug:
# 	   instance.slug = unique_slug_generator(instance)
