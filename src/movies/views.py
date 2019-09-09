import requests
from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .serializers import CreateMovieSerializer, MoviesSerializer, CommentsSerializer, TopMoviesSerializer
from .models import Comment, Movie
from .utils import transform_movie_details_to_db_format
from .settings import OMBD_KEY


def get_movie_info(title):
    key = OMBD_KEY
    try:
        r = requests.get(
            'http://www.omdbapi.com/?apikey={key}&t={title}'.format(key=key, title=title))
    except requests.exceptions.RequestException:
        return Response({"Error": "Can't connect to external API"},
                        status=status.HTTP_503_SERVICE_UNAVAILABLE)
    data = r.json()
    if 'Type' in data and data['Type'] != 'movie':
        return Response({"Error": "Requested content isn't a movie"},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(data=data, status=r.status_code)


class MoviesView(ListAPIView):

    serializer_class = MoviesSerializer
    queryset = Movie.objects.all()
    filter_backends = (
        filters.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter)
    search_fields = [
        'title',
        'actors',
        'genre',
        'director',
        'actors',
        'plot',
        'language',
        'country',
        'production']
    ordering_fields = ['year', 'metascore', 'imdbrating', 'imdbvotes']
    filterset_fields = ('year', 'director', 'title', 'type')

    def post(self, request):
        serializer = CreateMovieSerializer(data=request.data)
        if serializer.is_valid():
            external_response = get_movie_info(request.data['title'])
            if 'Error' in external_response.data or external_response.status_code != status.HTTP_200_OK:
                return Response(
                    external_response.data,
                    status=status.HTTP_400_BAD_REQUEST)
            movie_details = transform_movie_details_to_db_format(
                external_response.data)
            serializer = MoviesSerializer(data=movie_details)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsView(ListCreateAPIView):

    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('movie', 'date',)


class TopMoviesView(APIView):

    def get(self, request):
        serializer = TopMoviesSerializer(data=request.query_params)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
