from django.urls import path

from .views import MusicalWorkDetail, MusicalWorkList

urlpatterns = [
    path("", MusicalWorkList.as_view()),
    path("search_iswc/", MusicalWorkDetail.as_view(), name="search_iswc"),
]
