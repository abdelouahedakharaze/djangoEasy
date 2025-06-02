from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.SmallIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2030)])    
    
    def __str__(self):
        return self.title
    

























