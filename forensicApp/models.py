from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    image = models.ImageField(upload_to='media/service')

    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=120)
    exp = models.IntegerField()
    image = models.ImageField(upload_to='media/member')
    member_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    message = models.CharField(max_length=300)
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='media/feedback')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
    
class CarouselItem(models.Model):
    IMAGE = 'image'
    VIDEO = 'video'
    MEDIA_TYPE_CHOICES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    ]
    
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, default=IMAGE)
    image = models.ImageField(upload_to='carousel_images/', blank=True, null=True)
    video = models.FileField(upload_to='carousel_videos/', blank=True, null=True)
    caption_title = models.CharField(max_length=100)
    caption_subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50, default='Learn More')
    button_url = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.caption_title
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    
    class Meta:
        unique_together = ('user', 'post')
        
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)  # Add this line for a 'subscribed' boolean field
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject
