from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

