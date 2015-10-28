from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BookmarkManager(models.Manager):

    def filter_for_user(self, user):
        return self.filter(author=user)

    def filter_for_bookmarks(self, bookmark_id):
        return self.filter(bookmark_id=id)


class Bookmark(models.Model):
    author = models.ForeignKey(User)
    long_url = models.URLField()
    short_url = models.CharField(max_length=50 )
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    title = models.CharField(max_length=25)

    objects = BookmarkManager()

    @property
    def click_count(self):
        return self.click_set.all().count()

    class Meta:
        ordering = ["-created"]



class Click(models.Model):
    clicker = models.ForeignKey(User, null=True)
    bookmark = models.ForeignKey(Bookmark)
    created = models.DateTimeField(auto_now_add=True)

