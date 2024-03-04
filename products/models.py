from django.db import models
import uuid
from django.utils.text import slugify
from users.models import profile
 
class Make(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='models')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Car(models.Model):
    USED_NEW_OPTION = (
        ('New', 'New'),
        ('Used', 'Used'),
    )
    usednew = models.CharField(choices=USED_NEW_OPTION, max_length=10, null=True, blank=True)
    dealer = models.ForeignKey(profile,null=True, blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, blank=True, null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='cars')
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='model_makes',null=True, blank=True)
   # year = models.PositiveIntegerField()
    #price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True )
   # mileage = models.PositiveIntegerField()
    #engine = models.CharField(max_length=50, blank=True, null=True)
    #type = models.CharField(max_length=50, blank=True, null=True)
    #power = models.CharField(max_length=50, blank=True, null=True)
    #number_of_seats = models.CharField(max_length=50, blank=True, null=True)
    #doors = models.CharField(max_length=50, blank=True, null=True)
    #color = models.CharField(max_length=50, blank=True, null=True)
   # fuel = models.CharField(max_length=50, blank=True, null=True)
   # transmission = models.CharField(max_length=50, blank=True, null=True)
   # description = models.TextField()
   # vehicle_extras = models.TextField(max_length=2000,blank=True, null=True)
    image_1 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_2 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_3 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_4 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_5 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_6 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_7 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_8 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_9 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    image_10 = models.ImageField(null=True, blank=True, upload_to='static/cars_pic/', default='static/cars_pic/features-first-icon.png')
    featured = models.BooleanField(default=False)
    # Field to track page visits
    page_visits = models.PositiveIntegerField(null=True, blank=True, default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-page_visits']


        
class PartCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Part(models.Model):
    dealer = models.ForeignKey(profile,null=True, blank=True,on_delete=models.SET_NULL)
    category = models.ForeignKey(PartCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True,blank=True,)
    model = models.CharField(max_length=50, null=True,blank=True,)
    make = models.CharField(max_length=50, null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='static/sparepart_images')

    def __str__(self):
        return f'{self.category} - {self.name} - ${self.price:.2f}'
    
    class Meta:
        ordering = ['-created']
