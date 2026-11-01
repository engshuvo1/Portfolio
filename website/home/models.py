from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class meta:
        verbose_objects_plural = 'contact'

    def __str__(self):
        return self.name



class Project1 (models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image')
    http_link = models.URLField(max_length=200,default=True,null=True)


    def __str__(self):
         return self.title



class Images(models.Model):
    title = models.CharField(max_length=250,default=True,null=True)
    image = models.ImageField(upload_to='image')


    def __str__(self):
        return self.title