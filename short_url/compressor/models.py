from django.db import models

# Create your models here.


class Compression(models.Model):
    long_url = models.CharField(max_length=150)
    redirect_url = models.CharField(max_length=150)
    short_url = models.CharField(max_length=50)
    click_nums = models.PositiveIntegerField()