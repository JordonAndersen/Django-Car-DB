# pokemon_app/views.py
# We will import the following to read and return JSON data more efficiently
from rest_framework.views import APIView, Response

# We want to bring in our model
from .models import Car
from car_model_app.models import CarModel

# We will utilize serializer to turn our QuerySets into
# binary string
from django.core.serializers import serialize
from .serializers import CarSerializer

# Json.loads will turn binary strings into JSON data
import json


class AllCars(APIView):

    def get(self, request):
        cars = Car.objects.order_by('pk')
        cars_serialized = CarSerializer(cars, many=True)
        return Response(cars_serialized.data)


class SelectedCar(APIView):

    def get_car(self, id):

        if type(id) == int:
            return Car.objects.get(id = id)
        else:
            return Car.objects.get(registration_number = id)
        
    def get(self, request, id):

        car = self.get_car(id)
        car_serialized = CarSerializer(car, many=False)
        return Response(car_serialized.data)

    def put(self, request, id):

        car = self.get_car(id)

        



        
        
