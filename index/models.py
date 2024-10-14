from django.db import models

# Create your models here.


class HeroSection(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="hero_images", blank=True, null=True)
    button = models.URLField( max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
    
class HostelRommCard(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="hostelroom_card_images", blank=True, null=True)
    members = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name= models.CharField(max_length=50)
    image = models.ImageField(upload_to="testimonial", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    
    def __str__(self):
        return self.name

class Image_Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")
    category = models.ForeignKey(Image_Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.image.url
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    