from django.db import models

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to="banner", default="banner/default.jpg", blank=True)

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[0:500]