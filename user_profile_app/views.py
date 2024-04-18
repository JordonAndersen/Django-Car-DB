from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer
import json

class AllUserProfiles(APIView):
    
    def get(self, request):
        user_profiles = UserProfile.objects.order_by('pk')
        serializer = UserProfileSerializer(user_profiles, many=True)  
        return Response(serializer.data)
    
    def post(self, request, response):
        serializer = UserProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SelectUserProfiles(APIView):

    def get_user_profile(self, id):
        if isinstance(id, int):
            return UserProfile.objects.get(id=id)
        else:
            return UserProfile.objects.get(first_name=id)

    def get(self, request, id):
        user_profile = self.get_user_profile(id)
        json_user_profile = serialize('json', [user_profile])
        serialized_user_profile = json.loads(json_user_profile)
        return Response(serialized_user_profile.data)
    
    def put(self, request, id):
        user_profile = self.get_user_profile(id)
        if 'street_name' in request.data:
            user_profile.street_name = request.data['street_name']
        if 'street_number' in request.data:
            user_profile.street_number = request.data.street_number
        if 'zip_code' in request.data:
            user_profile.zip_code = request.data.zip_code
        if 'email' in request.data:
            user_profile.email = request.data.email
        if 'password' in request.data:
            user_profile.password = request.data.password


    def delete(self, request, id):
        user_profile = self.get_user_profile(id)
        serialized_user_profile = UserProfileSerializer(user_profile, many=False)
        first_name = serialized_user_profile.data[0]['account_id']['first_name']
        last_name = serialized_user_profile.data[0]['account_id']['last_name']
        user_profile.delete()
        return Response(f"User account for {first_name} {last_name} has been deleted.")