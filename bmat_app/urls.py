from django.urls import path

from .views import MusicalWorkDetail, MusicalWorkDetailByForm, MusicalWorkList

urlpatterns = [
    path("", MusicalWorkList.as_view()),
    path("search_iswc/", MusicalWorkDetailByForm.as_view(), name="search_iswc"),
    path("<str:iswc>/", MusicalWorkDetail.as_view()),
]
