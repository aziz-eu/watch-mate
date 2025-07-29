from django.urls import path
from watchmate_app.api.views import WatchListAV, WatchDetailsAV, StrimingPlatfromListAV

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchDetailsAV.as_view(), name="movie-details"),
    path("streming/", StrimingPlatfromListAV.as_view(), name="streming-list"),
]
