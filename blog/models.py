import datetime

import pytz
from django.db import models
from django.utils import timezone



class Category(models.Model):
    title = models.CharField(max_length=500, unique=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=2000)
    slug = models.CharField(max_length=2000,unique=True)
    read_time = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='blog', on_delete=models.CASCADE)
    image1 = models.FileField(upload_to='images/', null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    image2 = models.FileField(upload_to='images/', null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    image3 = models.FileField(upload_to='images/', null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    image4 = models.FileField(upload_to='images/', null=True, blank=True)
    body4 = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    post = models.BooleanField(default=False)
    post_published = models.DateTimeField(null=True, blank=True)



    def save(self, *args, **kwargs):
        if self.post_published:
            now = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
            time_difference = self.post_published - now
            if time_difference.total_seconds() <= 0:
                # The post_published datetime is in the past or present,
                # so the post is active
                self.post = True
            else:
                # The post_published datetime is in the future,
                # so the post will become active after one hour
                self.post = False
        else:
            # If post_published is not set, the post is not active
            self.post = False

        return super().save(*args, **kwargs)




























    # def save(self, *args, **kwargs):
    #     if self.post_published and self.post_published <= datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')):
    #         self.post = True
    #     else:
    #         self.post = False
    #     return super().save(*args, **kwargs)




class Spotlight(models.Model):
    title = models.CharField(max_length=2000)
    image1 = models.FileField(upload_to='images/', null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    image2 = models.FileField(upload_to='images/', null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
