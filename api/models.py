from django.db import models

class UserAccount(models.Model):    
    email = models.CharField( max_length=50,unique=True)
    name = models.CharField( max_length=50)
    surname = models.CharField( max_length=50)
    password = models.CharField( max_length=50)

 


class MessagePost(models.Model):         
    name = models.CharField(default="" ,max_length=50)    
    message = models.CharField( default= "" ,max_length=50)
 