from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Director(models.Model):
    name= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # movies_directed - OTM

class Movie(models.Model):
    title= models.CharField(max_length=255)
    year= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    directed_by = models.ForeignKey(Director, related_name="movies_directed", on_delete = models.CASCADE)
    # actors - MTM
    def __repr__(self):
        return f"<movie {self.id}, title:{self.title}>"

    def __str__(self):
        return f"{self.title}, {self.id}"



class Actor(models.Model):
    name= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movies_acted_in = models.ManyToManyField(Movie, related_name="actors")


