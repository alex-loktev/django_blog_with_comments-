from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length = 60)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField('Tags', related_name = 'posts',  blank = True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PostDetail', kwargs = {'pk': self.pk})

class Tags(models.Model):
    title = models.CharField(max_length = 60, unique = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('TagDetail', kwargs = {'pk': self.pk})

class Comments(models.Model):
    logname = models.CharField(max_length = 50)
    text = models.TextField()
    post = models.ForeignKey('Post', on_delete = models.CASCADE, related_name = 'comments')
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-created',)
