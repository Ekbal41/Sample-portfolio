from django.db import models


class Project(models.Model):

    photo = models.ImageField(upload_to = "projectphoto/")
    name=models.CharField(max_length=300)
    date=models.DateTimeField(auto_now=True)
    link=models.CharField(max_length=300)
    description=models.TextField(max_length=500)
    
    
    
    
    def __str__(self):
        return self.name
    
