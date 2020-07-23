from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    weight = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'

class Feed(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tag = models.ManyToManyField('Tag')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

class Image(models.Model):
    feed = models.ForeignKey('Feed', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.feed}'

class Like(models.Model):
    feed = models.ForeignKey('Feed', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    like = models.BooleanField()

    def __str__(self):
        return f'{self.feed}'




