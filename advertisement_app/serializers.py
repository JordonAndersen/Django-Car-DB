# move_app/serializers.py
from rest_framework import serializers
from .models import Advertisement
from car_app.serializers import CarSerializer
from app_user_app.serializers import AppUserSerializer

class AdvertisementSerializer(serializers.ModelSerializer):
    

    car_id = CarSerializer(many=False)
    seller_account_id = AppUserSerializer(many=False)

    class Meta:

        model = Advertisement
        fields = ('advertisement_date', 'seller_account_id', 'car_id')