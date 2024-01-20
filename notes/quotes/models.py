from django.db import models
from users.models import Profile  

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[:20]}... - {self.author}'