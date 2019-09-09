from django.test import TestCase, Client
from django.urls import reverse
from unittest import mock
from datetime import date
from .serializers import CommentsSerializer
from .models import Movie, Comment
from .test_data import movie_dict, comment_dict, movie_list, comment_list


class MovieViewTest(TestCase):

    def setUp(self):
        self.movie_dict = movie_dict
        self.client = Client()


    @mock.patch('movies.views.get_movie_info')
    def test_post_movie_correct(self, mocked_ext):
        mocked_response = mock.MagicMock()
        mocked_response.data = self.movie_dict
        mocked_response.status_code = 200
        mocked_ext.return_value = mocked_response
        response = self.client.post(reverse('movies'), {'title': 'Test movie'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], self.movie_dict['title'])

    @mock.patch('movies.views.get_movie_info')
    def test_post_movie_wrong_response(self, mocked_ext):
        mocked_response = mock.MagicMock()
        mocked_response.data = {'Error': 'TestError'}
        mocked_response.status_code = 503
        mocked_ext.return_value = mocked_response
        response = self.client.post(reverse('movies'), {'title': 'Test movie'})
        self.assertNotEqual(response.status_code, 200)
    
    def test_post_movie_no_title(self):
        response = self.client.post(reverse('movies'), {'notitle': 'Test movie'})
        self.assertNotEqual(response.status_code, 200)

    def test_get_movies(self):
        Movie(**self.movie_dict).save()
        response = self.client.get(reverse('movies'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['title'], self.movie_dict['title'])


class CommentViewTest(TestCase):

    def setUp(self):
        movie = Movie(**movie_dict)
        movie.save()
        self.id = movie.id
        comment_dict['movie'] = self.id
        serializer = CommentsSerializer(data=comment_dict)
        serializer.is_valid()
        serializer.save()
        self.client = Client()
    
    def test_get_comments(self):
        response = self.client.get(reverse('comments'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['comment'], comment_dict['comment'])
    
    def test_post_comment(self):
        response = self.client.get(reverse('comments'), {'comment': 'test', 'movie':self.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['date'], date.today().strftime('%Y-%m-%d'))


class TopMoviesTest(TestCase):

    def setUp(self):
        for movie in movie_list:
            Movie(**movie).save()
        for comment in comment_list:
            serializer = CommentsSerializer(data=comment)
            serializer.is_valid()
            serializer.save()
        self.client = Client()
        self.start_date = '2019-09-08'
        self.end_date = '2019-09-10'
        self.end_date_short = '2019-09-09'
        self.expected_response = [{'movie_id': 102, 'total_comments': 5, 'rank': 1}, {'movie_id': 101, 'total_comments': 2, 'rank': 2},
         {'movie_id': 100, 'total_comments': 2, 'rank': 2}]
        self.expected_response_short = [{'movie_id': 101, 'total_comments': 2, 'rank': 1}, {'movie_id': 100, 'total_comments': 2, 'rank': 1},
         {'movie_id': 102, 'total_comments': 1, 'rank': 2}]

    
    def test_get_top(self):
        response = self.client.get(reverse('top'), {'start_date':self.start_date, 'end_date':self.end_date})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.expected_response)
        response = self.client.get(reverse('top'), {'start_date':self.start_date, 'end_date':self.end_date_short})
        self.assertEqual(response.data, self.expected_response_short)
