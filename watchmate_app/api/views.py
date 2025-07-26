from watchmate_app.models import Movie
from watchmate_app.api.serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

def movie_by_id(resqust):
    pass