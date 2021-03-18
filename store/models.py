from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    icon = models.FileField(upload_to='static/icons', null=True, blank=True)
    cover = models.FileField(upload_to='static/icons')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=250)
    icon = models.FileField(upload_to="static/icons", null=True, blank=True)
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name

class Ad(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image1 = models.FileField(upload_to="static/ads", null=True, blank=True)
    image2 = models.FileField(upload_to="static/ads", null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title