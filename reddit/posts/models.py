from django.db import models

from uuid import uuid4
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver

 
def upload_location(instance, filename):

	file_path = 'post/{title}-{filename}'.format(title=str(instance.title),filename=filename)
	return file_path

	#create your models here
class Post(models.Model):

	title            =models.CharField(max_length=255,null=False,blank=False)
	body             =models.TextField(max_length=2000,null=False,blank=False)
	image            =models.ImageField(upload_to =upload_location)
	date_published   =models.DateField(auto_now=True,verbose_name="date published")
	date_updated     =models.DateField(auto_now=True,verbose_name="date_updated")
	slug 	   	   	 =models.SlugField(blank=True, unique=True)

	def __str__(self):
	 return self.title

class Task(models.Model):
	title         = models.CharField(max_length = 200)
	completed     = models.BooleanField(default=False, blank=True, null=True)
	

@receiver(post_delete)
def submission_delete(instance,**kwargs):
	instance.image.delete(False)

