# move_app/serializers.py
from rest_framework import serializers
from .models import Advertisement
from car_app.serializers import CarSerializer
from app_user_app.serializers import AppUserSerializer
from car_model_app.serializers import CarModelSerializer
from car_app.models import Car
from app_user_app.models import AppUser
from car_model_app.models import CarModel

class AdvertisementSerializer(serializers.ModelSerializer):
    

    car_id = CarSerializer(many=False)
    seller_account_id = AppUserSerializer(many=False)
    

    class Meta:

        model = Advertisement
        fields = ('advertisement_date', 'seller_account_id', 'car_id')


    def create(self, validated_data):

       
        car_data = validated_data.pop('car_id')
        app_user_data = validated_data.pop('seller_account_id')
        car_model_data = car_data.pop('car_model_id')
        

        advertisement = Advertisement.objects.create(**validated_data)

        car = Car.objects.create(**car_data)
        car_model = CarModel.objects.create(**car_model_data)
        car.car_model_id.add(car_model)

        app_user = AppUser.objects.create(**app_user_data)

        advertisement.car_id.add(car)
        advertisement.seller_account_id.add(app_user)

        return advertisement