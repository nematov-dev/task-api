from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class ProductsModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="posts")
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title