from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=10000)
    create_date=models.DateTimeField(default=datetime.now,blank=True)
class magic(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=10000)