from django.forms import ModelForm
from django.db import models

class Slideshow(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Slideshow')
    description = models.TextField(null=True,blank=True)
    link = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title
    
class team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team')
    job_title = models.CharField(max_length=100,null=True,blank=True)
    link= models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Research(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Research')
    description = models.TextField()
    link = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title
    
class Achievement(models.Model):
    title = models.CharField(max_length=200)
    Field1 = models.CharField(max_length=200,null=True,blank=True)
    Field1Desc = models.CharField(max_length=200,default='Happy customers')
    Field2 = models.CharField(max_length=200,null=True,blank=True)
    Field2Desc = models.CharField(max_length=200,default='Issues Solved')
    Field3 = models.CharField(max_length=200,null=True,blank=True)
    Field3Desc = models.CharField(max_length=200,default='Projects completed')
    Field4 = models.CharField(max_length=200,null=True,blank=True)    
    Field4Desc = models.CharField(max_length=200,default='Awwards Won')

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email