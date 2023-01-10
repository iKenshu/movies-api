from django.utils.text import slugify
from django.db import models

from users.models import User


class Movie(models.Model):
    title = models.CharField(max_length=140)
    synopsis = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    director = models.CharField(max_length=140)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Collection(models.Model):
    name = models.CharField(max_length=140)
    is_private = models.BooleanField(default=False)
    movies = models.ManyToManyField(Movie, related_name="collections")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
