from watchmate_app.models import WatchList, StreamPlatform
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StreamPlatformSerializers, WatchListSerializers
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StrimingPlatfromListAV(APIView):

    def get(self, request):
        platfroms = StreamPlatform.objects.all()
        serialization = StreamPlatformSerializers(platfroms, many=True)
        return Response(serialization.data)

    @swagger_auto_schema(request_body=StreamPlatformSerializers)
    def post(self, request):

        serializer = StreamPlatformSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class StreamingPlatformDetailsAV(APIView):

    def get(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializers(platform)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StreamPlatformSerializers)
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializers(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        watch_list = WatchList.objects.all()
        serialization = WatchListSerializers(watch_list, many=True)
        return Response(serialization.data)

    @swagger_auto_schema(request_body=WatchListSerializers)
    def post(self, request):

        serializer = WatchListSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class WatchDetailsAV(APIView):

    def get(self, request, pk):
        watch_list = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializers(watch_list)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=WatchListSerializers)
    def put(self, request, pk):
        watch_list = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializers(watch_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        watch_list = WatchList.objects.get(pk=pk)
        watch_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view()
# def movie_list(request):
#     movies = WatchList.objects.all()
#     serializer = WatchListSerializers(movies, many=True)
#     return Response(serializer.data)
# @api_view()
# def movie_by_id(resqust, pk):
#     watch_list = WatchList.objects.get(pk = pk)
#     serializer = WatchListSerializers(watch_list)
#     return Response(serializer.data)
