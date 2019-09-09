from django.db import models
from django.contrib.postgres.fields import ArrayField, HStoreField

SMALL_CHARFIELD_SIZE = 25
MEDIUM_CHARFIELD_SIZE = 60

class Movie(models.Model):
    title = models.TextField(unique=True)
    year = models.IntegerField()
    rated = models.CharField(max_length=SMALL_CHARFIELD_SIZE)
    runtime = models.CharField(max_length=SMALL_CHARFIELD_SIZE)
    genre = models.TextField()
    director = models.TextField()
    actors = models.TextField()
    plot = models.TextField()
    language = models.CharField(max_length=MEDIUM_CHARFIELD_SIZE)
    country = models.TextField()
    awards = models.TextField()
    poster = models.TextField()
    ratings = ArrayField(base_field=HStoreField(), blank=True)
    metascore = models.CharField(max_length=SMALL_CHARFIELD_SIZE)
    imdbrating = models.FloatField()
    imdbvotes = models.IntegerField()
    imdbid = models.CharField(max_length=SMALL_CHARFIELD_SIZE)
    type = models.CharField(max_length=SMALL_CHARFIELD_SIZE)
    dvd = models.CharField(max_length=SMALL_CHARFIELD_SIZE)
    boxoffice = models.CharField(max_length=MEDIUM_CHARFIELD_SIZE)
    production = models.CharField(max_length=MEDIUM_CHARFIELD_SIZE)
    website = models.TextField()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField()

