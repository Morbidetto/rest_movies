import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
frrom .serializers import CreateMovieSerializer


@api_view(['GET'])
def external_moviedb_view(request):
    if request.method == 'GET':
        title = request.data['title']
        r = requests.get('http://www.omdbapi.com/?apikey={key}&t={title}'.format(key, title))
        if r.status_code == 200:
                data = r.json()
                return Response(data, status=status.HTTP_200_OK)
        return Response({"error": "Request failed"}, status=r.status_code)


class MoviesView(APIView):

    def get(self, request):
        pass

    def post(self,request):
        serializer = CreateMovieSerializer(data=request.data)
        if serializer.is_valid():
            external_response = external_moviedb_view(request)
            serializer = 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
