from rest_framework import serializers
from datetime import date
from .models import Movie, Comment

class CreateMovieSerializer(serializers.Serializer):
    title = serializers.CharField()


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    date = serializers.DateField(default=date.today())
    class Meta:
        model = Comment
        fields = '__all__'