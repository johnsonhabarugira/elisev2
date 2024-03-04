from django.db import models

# Create your models here.

class BannerImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title