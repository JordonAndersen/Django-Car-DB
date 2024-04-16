from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from rest_framework.views import APIView, Response
from .models import Advertisement
from car_app.models import Car
from app_user_app.models import AppUser
from .serializers import AdvertisementSerializer
import json


# Create your views here.
# def advertisement_response(request):
#     return render(request)

class Advertisements(APIView):
    def get(self, request):
        Advert = Advertisement.objects.order_by('advertisement_date')
        serializer = AdvertisementSerializer(Advert, many=True)
        return Response(serializer.data)