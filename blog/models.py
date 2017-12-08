from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    topic = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    post = models.ForeignKey('post')
    def __str__(self):
        return 'Комент %s до %s' % (self.author, self.post)
