from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_movie(request, pk):
    try:
        movies = Movie.objects.get(id=pk)
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    except:
        return Response({'error': 'requested pk does not exist'})