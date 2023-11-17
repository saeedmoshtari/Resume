from django.db import models
from django.db.models import JSONField


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    feature = JSONField()
    variety = models.ManyToManyField('Variety', related_name='products')

    def __str__(self):
        return self.name


class Variety(models.Model):
    color = models.CharField(max_length=200)
    available_variety = JSONField()
    images = models.ManyToManyField('Image', related_name='varieties')

    def __str__(self):
        return self.color


class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.url
