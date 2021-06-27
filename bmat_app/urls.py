from django.urls import path

from .views import (MusicalWorkDetail, MusicalWorkDetailBrowsableAPI,
                    MusicalWorkList)

urlpatterns = [
    path("", MusicalWorkList.as_view()),
    path("search_iswc/", MusicalWorkDetail.as_view(), name="search_iswc"),
    path("<str:iswc>/", MusicalWorkDetailBrowsableAPI.as_view()),
]
