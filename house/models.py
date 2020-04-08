from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    image_tag.short_description = 'Image'


class House(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=255)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    slug = models.SlugField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    rent = models.IntegerField(blank=True)
    detail = RichTextUploadingField(blank=True)
    status = models.CharField(blank=True, max_length=10, choices=STATUS)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    area = models.IntegerField(blank=True, )
    location = models.CharField(blank=True, max_length=255)
    room = models.CharField(blank=True, max_length=255)
    buildingFloor = models.IntegerField(blank=True, )
    floorLocation = models.IntegerField(blank=True, )
    furnished = models.CharField(blank=True, max_length=10, choices=STATUS)
    balconied = models.CharField(blank=True, max_length=10, choices=STATUS)
    heating = models.CharField(blank=True, max_length=255)
    withintheSite = models.CharField(blank=True, max_length=10, choices=STATUS)
    fromWho = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    image_tag.short_description = 'Image'


class Images(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    image_tag.short_description = 'Image'

