from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=200, null=True,blank=True)
    email = models.EmailField(max_length=500, blank=False,null=False)
    title = models.CharField(max_length=50,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(blank=True,null=True,upload_to='static/profile_pic/', default='static/profile_pic/features-first-icon.png')
    Social_twitter = models.CharField(max_length=200, null=True,blank=True)
    Social_facebook = models.CharField(max_length=200, null=True,blank=True)
    Social_whatsapp = models.CharField(max_length=200, null=True,blank=True)
    address_location = models.CharField(max_length=200, null=True,blank=True)
    phone_number = models.CharField(max_length=200, null=True,blank=True)
    featured = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    def __str__(self):
        return str(self.user.username)
    
