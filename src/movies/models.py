from django.db import models

class Movie(models.Model):
    title = models.TextField()
    year = models.IntegerField()
    rated = models.CharField()
    runtime = models.IntegerField()
    genre = models.TextField()
    director = models.TextField()
    actors = models.TextField()
    plot = models.TextField()
    language = models.CharField()
    country = models.CharField()
    awards = models.TextField()


class Comment(models.Model):
    movie = models.ForeignKey(Movie)
    comment = models.TextField()

