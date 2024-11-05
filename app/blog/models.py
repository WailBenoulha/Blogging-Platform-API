from datetime import timezone
from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils.translation import gettext as _


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email
   
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255,blank=True)    
    content = models.TextField()
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='author',editable=False)

    def __str__(self):
        return self.title