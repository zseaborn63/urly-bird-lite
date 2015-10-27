from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Bookmark(models.Model):
    author = models.ForeignKey(User)
    long_url = models.TextField()
    redirect_url = models.CharField(max_length=150)
    short_url = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)



class Click(models.Model):
    clicker = models.ForeignKey(User, null=True)
    bookmark = models.ForeignKey(Bookmark)
    created = models.DateTimeField(auto_now_add=True)
    click_nums = models.PositiveIntegerField()