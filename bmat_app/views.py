import json

from django.shortcuts import render
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MusicalWork
from .serializers import MusicalWorkSerializer


class MusicalWorkList(generics.ListAPIView):
    # API endpoint that allows to view all the MusicalWork stored in db.
    queryset = MusicalWork.objects.all()  # [:20]
    serializer_class = MusicalWorkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "iswc"
    ]  #  http://localhost:8000/?search=T9204649558 very flexible: match substring, not case-sensitive...


class MusicalWorkDetail(generics.RetrieveAPIView):
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer
    lookup_field = "iswc"  #  http://localhost:8000/T9204649558/?format=json


class MusicalWorkDetailByForm(APIView):
    def get(self, request, format=None):
        if "iswc" in request.GET:
            iswc = request.GET["iswc"]
            musical_work = MusicalWork.objects.filter(iswc=iswc).all()
            musical_work_serializer = MusicalWorkSerializer(musical_work, many=True)
            response = musical_work_serializer.data
            response = json.loads(json.dumps(response))
            return Response(response)
        return render(request, "search.html", {})  # http://localhost:8000/search_iswc/
