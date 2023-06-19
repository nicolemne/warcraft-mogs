from django.db import models
from django.contrib.auth.models import User
from django import forms
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Post(models.Model):
    '''
    Post model to feature a blog post and its content
    '''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    category = models.CharField(max_length=200, default="undefined")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    '''
    Comment model to feature a blog comment and its content
    '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(verbose_name="")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Category(models.Model):
    '''
    Category model to display a category/tag on each post
    '''
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Contact(models.Model):
    '''
    Contact form
    '''
    name = models.CharField(max_length=150)
    email = models.EmailField()
    title = models.CharField(max_length=200, unique=False)
    message = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name
