from django.contrib import admin

# Register your models here.
from todo.models import Task, Tile

admin.site.register(Task)
admin.site.register(Tile)
