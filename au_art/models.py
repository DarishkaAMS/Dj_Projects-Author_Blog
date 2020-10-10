from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "authors"

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    title = models.CharField(max_length=255)
    article = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "articles"

    def __str__(self):
        return f"{self.author} - {self.title[0:25]}. created on {self.created_on}"
