from django.db import models
from django.utils import timezone
from jsonfield import JSONField

class Post(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Annotation(models.Model):
    URI = models.TextField()
    surfaceForm = models.TextField()
    offset = models.TextField()
#    attributeValues = models.TextField()
    label = models.TextField()
    p = models.ForeignKey(Post)

    def __str__(self):
        return self.URI

    class Meta:
        ordering = ('URI',)
   
