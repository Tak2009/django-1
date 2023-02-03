from django.contrib import admin

# Register your models here.
from daisy.models import Pic, Comment

admin.site.register(Pic)
admin.site.register(Comment)