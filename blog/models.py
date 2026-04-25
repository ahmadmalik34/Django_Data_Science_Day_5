from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

        class Meta:
            verbose_name_plural="Categories"

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='posts')
    categories=models.ManyToManyField(Category,related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created_at']
        verbose_name='Blog Post'
        verbose_name_plural='Blog Posts'