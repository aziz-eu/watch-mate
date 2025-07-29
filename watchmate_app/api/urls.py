from django.urls import path
from watchmate_app.api.views import (
    WatchListAV,
    WatchDetailsAV,
    StrimingPlatfromListAV,
    StreamingPlatformDetailsAV,
)

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchDetailsAV.as_view(), name="movie-details"),
    path(
        "strimingplatform/",
        StrimingPlatfromListAV.as_view(),
        name="strimingplatform-list",
    ),
    path(
        "strimingplatform/<int:pk>",
        StreamingPlatformDetailsAV.as_view(),
        name="strimingplatform-details",
    ),
]
