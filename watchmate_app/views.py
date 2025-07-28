# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {"movies" :  list(movies.values())}
#     return JsonResponse(data)

# def movie_by_id(request, pk):
#     movie = Movie.objects.get(pk = pk)
#     date = {
#         "name" : movie.name,
#         "description": movie.description,
#         "isActive" : movie.isActive
#         }
#     return JsonResponse(date)
