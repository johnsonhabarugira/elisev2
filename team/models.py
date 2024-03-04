from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(blank=True,null=True,upload_to='static/team_pic/', default='static/profile_pic/features-first-icon.png')
    Social_twitter = models.CharField(max_length=200, null=True,blank=True)
    Social_facebook = models.CharField(max_length=200, null=True,blank=True)
    Social_instagram = models.CharField(max_length=200, null=True,blank=True)
    Social_whatsapp = models.CharField(max_length=200, null=True,blank=True)
    phone_number = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.name
