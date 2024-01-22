from django.db import models
from users.models import Profile  

class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='author_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[:20]}... - {self.author}'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
	