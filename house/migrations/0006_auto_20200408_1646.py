# Generated by Django 3.0.3 on 2020-04-08 13:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20200407_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='area',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='balconied',
            field=models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
        migrations.AlterField(
            model_name='house',
            name='buildingFloor',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='floorLocation',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='fromWho',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='furnished',
            field=models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
        migrations.AlterField(
            model_name='house',
            name='heating',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='rent',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='room',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
        migrations.AlterField(
            model_name='house',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='withintheSite',
            field=models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
