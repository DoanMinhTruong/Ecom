from django.db import models
from user.models import MyUser
from book.models import Book
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(MyUser , on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)