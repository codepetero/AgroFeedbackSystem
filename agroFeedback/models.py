from django.db import models

#from django.db import models
from authentication.models import User



class Farmers(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50, null=True)
    last_name=models.CharField(max_length=50, null=True)
    reg_No=models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    location = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.reg_No

class Sacco(models.Model):
    sacco_id=models.AutoField(primary_key=True)
    sacco_name=models.TextField()

    def __str__(self):
        return self.sacco_name

    

class Feedback(models.Model):
    id=models.AutoField(primary_key=True)
    farmer=models.ForeignKey(Farmers, on_delete=models.CASCADE , null=True)
    feedback_message = models.TextField()
    sacco=models.ForeignKey(Sacco, on_delete=models.CASCADE,null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Feedback_reply(models.Model):
    feedback_reply =models.TextField()
    feedback_message=models.ForeignKey(Feedback, on_delete=models.CASCADE, null=True)
    

class Major_Area(models.Model):
    category=models.CharField(max_length=100)
    


    

   
    
    


