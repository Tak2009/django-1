from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
# from django.conf import settings

class Pic(models.Model) :
    title = models.CharField(
            max_length=200,
            null=True,
    )
    # Picture
    pic = models.ImageField(upload_to='', null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title