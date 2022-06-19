from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    Author = models.(Post, on_delete =models.CASCADE)
    Created_date = models.DateTimeField(default = datetime.today)
    Published_date: models.DateTimeField(default = datetime.today)
