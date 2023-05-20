from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.username
    
class userRants(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    rantText = models.CharField(max_length=750)
    rantDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.username, self.rantText, self.rantDate)