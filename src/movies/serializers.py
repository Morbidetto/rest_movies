from django.db.models import Q, Count
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


class TopMoviesSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        start_date = validated_data.pop("start_date")
        end_date = validated_data.pop("end_date")
        movies = Movie.objects.annotate(
            total_comments=Count(
                'comment',
                filter=Q(
                    comment__date__range=(
                        start_date,
                        end_date)))).order_by('-total_comments')
        result_list = []
        current_rank = 1
        previous_comments = -1
        for movie in movies:
            if movie.total_comments < previous_comments:
                current_rank += 1
            movie_dict = {
                'movie_id': movie.id,
                'total_comments': movie.total_comments,
                'rank': current_rank
            }
            result_list.append(movie_dict)
            previous_comments = movie.total_comments
        return result_list
