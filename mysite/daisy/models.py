from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
from django.conf import settings #https://learndjango.com/tutorials/django-best-practices-referencing-user-model

class Pic(models.Model) :
    title = models.CharField(
            max_length=200,
            null=True,
    )
    # Picture
    pic = models.ImageField(upload_to='', null=True)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Comment', related_name='comments_owned')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model) :
    comment = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    pic = models.ForeignKey(Pic, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.comment) < 15 : return self.comment
        return self.comment[:11] + ' ...'