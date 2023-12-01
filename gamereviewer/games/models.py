from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = "games"
class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    class Meta:
        db_table = "reviews"
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    class Meta:
        db_table = "comments"
