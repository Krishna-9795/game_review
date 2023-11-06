from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    approved = models.BooleanField(default=False)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()

