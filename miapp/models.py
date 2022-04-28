from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    public = models.BooleanField(default=False)
    image = models.ImageField(default='null', upload_to = "articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.content} - Public:{self.public} - {self.created_at}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()