from django.contrib import admin

# Register your models here.

from onestop.models import Recipe, Note, Favo

admin.site.register(Recipe)
admin.site.register(Note)
admin.site.register(Favo)