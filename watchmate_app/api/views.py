from watchmate_app.models import Movie
from watchmate_app.api.serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import response
from rest_framework.views import APIView
from .serializers import MovieSerializers
from rest_framework import status


class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serialization = MovieSerializers(movies, many=True)
        return Response(serialization.data)

    def post(self, request):

        serializer = MovieSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MovieDetailsAV(APIView):

    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view()
# def movie_list(request):
#     movies = Movie.objects.all()
#     serializer = MovieSerializers(movies, many=True)
#     return Response(serializer.data)
# @api_view()
# def movie_by_id(resqust, pk):
#     movie = Movie.objects.get(pk = pk)
#     serializer = MovieSerializers(movie)
#     return Response(serializer.data)
