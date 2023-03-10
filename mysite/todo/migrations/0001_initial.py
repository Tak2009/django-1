# Generated by Django 4.0.7 on 2023-02-15 15:24

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('LIVE', 'Live'), ('PEND', 'Pending'), ('ARCH', 'Archived')], default='LIVE', max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')])),
                ('order_number', models.IntegerField(help_text='Integer field. input the order number please')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('task_type', models.CharField(blank=True, help_text='Such as survey, discussion, diary', max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tile', models.ForeignKey(help_text='Tasks need to be assigned to a tile and thus you need to create the tile first', on_delete=django.db.models.deletion.CASCADE, to='todo.tile')),
            ],
        ),
    ]
