from rest_framework import serializers
from .models import Car
from car_model_app.serializers import CarModelSerializer

class CarSerializer(serializers.ModelSerializer):

    car_model_id = CarModelSerializer(many=False)
    class Meta:
        model = Car
        fields = ('number_of_owners', 'car_model_id', 'registration_number', 'manufacture_year', 'number_of_doors', 'mileage')


