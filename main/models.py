from django.db import models


# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=100)
    
    def __str__(self):
        return self.language

class Country(models.Model):
    country = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language)
    
    def __str__(self):
        return self.country
