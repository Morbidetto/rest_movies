from django.urls import path

from .views import MoviesView, CommentsView, TopMoviesView

urlpatterns = [
    path('movies/', MoviesView.as_view(), name='movies'),
    path('comments/', CommentsView.as_view(), name='comments'),
    path('top/', TopMoviesView.as_view(), name='top'),
]
