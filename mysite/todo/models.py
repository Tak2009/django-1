from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from ckeditor.fields import RichTextField


class Tile(models.Model) :
    LIVE = 'LIVE'
    PEND = 'PEND'
    ARCH = 'ARCH'
    STATUS_CHOICES = [
        (LIVE, 'Live'),
        (PEND, 'Pending'),
        (ARCH, 'Archived'),
    ]
    launch_date = models.DateTimeField(blank=False)
    status = models.CharField(
        max_length=4,
        choices= STATUS_CHOICES,
        default=LIVE,
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.launch_date.strftime('%m-%d-%y %H:%M:%S')


class Task(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    order_number = models.IntegerField(blank=False,
                                    help_text='Integer field. input the order number please')
    description = RichTextField(blank=True, null=True)
    task_type = models.CharField(max_length=256, null=True, blank=True,
                                    help_text='Such as survey, discussion, diary')
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE,
                                    help_text='Tasks need to be assigned to a tile and thus you need to create the tile first')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




