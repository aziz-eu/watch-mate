from  django.urls import path
from watchmate_app.api.views import movie_list, movie_by_id

urlpatterns = [
    path('list/', movie_list, name="movie-list"),
    path('<int:pk>', movie_by_id, name="movie-details" )
]
