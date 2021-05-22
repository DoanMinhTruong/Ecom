from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 255 , unique = True)
    price = models.FloatField(verbose_name='price') 
    author = models.CharField(max_length= 255) 
    intro = models.TextField()
    img = models.ImageField(upload_to = 'uploads/')