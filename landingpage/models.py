from django.db import models

# Create your models here.


class ContactUs(models.Model):
    fullName = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    message = models.TextField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.email


class Team(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    read_more_link = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class SocialMediaLinks(models.Model):
    instagram = models.CharField(max_length=1000, null=True, blank=True)
    twitter = models.CharField(max_length=1000, null=True, blank=True)
    facebook = models.CharField(max_length=1000, null=True, blank=True)
    rss = models.CharField(max_length=1000, null=True, blank=True)
    tumblr = models.CharField(max_length=1000, null=True, blank=True)
    linkedIn = models.CharField(max_length=1000, null=True, blank=True)
