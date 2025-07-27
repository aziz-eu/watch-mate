from watchmate_app.models import Movie
from watchmate_app.api.serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)
@api_view()
def movie_by_id(resqust, pk):
    movie = Movie.objects.get(pk = pk)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)