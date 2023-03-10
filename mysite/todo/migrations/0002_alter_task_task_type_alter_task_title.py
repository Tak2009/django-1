# Generated by Django 4.0.7 on 2023-02-15 23:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(default='survey', help_text='Such as survey, discussion, diary', max_length=256, validators=[django.core.validators.MinLengthValidator(2, 'Task type must be greater than 2 characters')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=256, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')]),
        ),
    ]
