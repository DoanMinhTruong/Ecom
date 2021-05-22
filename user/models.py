from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username = username,
            email= self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username , email, password):
        user = self.create_user(
            username,
            email,
            password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class MyUser(AbstractBaseUser):
    username = models.CharField(verbose_name = 'user name' , max_length = 255 , unique = True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    password = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email' , 'password']
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin