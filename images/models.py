from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    name = models.CharField(max_length =30)
    bio = models.CharField(max_length=300)
    contact= models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='Images/', blank=True)
    
   
    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['profile']


    def save_profile(self):
         self.save()  
         
    def delete_profile(self):
         self.delete()  

    def display_profile(self):
         self.display()

    def update_profile(self):
         self.update()  

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_by_name(cls,search_term):
        profiles = cls.objects.filter(user_name__icontains=search_term)
        return profiles       

    

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length =70) 
    image = models.ImageField(upload_to = 'images/')
    detail= models.TextField()
    poster = models.CharField(max_length=30)
    link= models.TextField()
    
  
   
   

    def __str__(self):
        return self.title

      

    def save_project(self):
         self.save()  
         
    
    @classmethod
    def get_project(cls):
        project = cls.objects.all()
        return project   

    def delete_project(self):
        self.delete()   

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project       


    
       

    