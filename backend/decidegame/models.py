from django.db import models

# Create your models here.

# the Game model
# defines how game info should be stored in database
class Game(models.Model):
    title = models.CharField(max_length=336)
    summary = models.TextField()
    
    def __str__(self) -> str:
        return self.title
