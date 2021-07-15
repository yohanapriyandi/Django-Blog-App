from django.db import models
from django.db.models.fields import CharField, TextField

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_addes = models.DateTimeField(auto_now_add=True)