# move_app/serializers.py
from rest_framework import serializers
from .models import AppUser
from user_profile_app.serializers import UserProfileSerializer

class AppUserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only = True)
    class Meta:
        model = AppUser
        fields = ('account_id', 'first_name', 'last_name', 'email', 'user_profile' )