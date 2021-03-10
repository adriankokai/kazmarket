from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    icon = models.FileField(upload_to='static/icons', null=True, blank=True)
    cover = models.FileField(upload_to='static/icons')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name