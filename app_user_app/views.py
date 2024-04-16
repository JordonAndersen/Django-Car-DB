# pokemon_app/views.py
# We will import the following to read and return JSON data more efficiently
from rest_framework.views import APIView, Response

# We want to bring in our model
from .models import AppUser

# We will utilize serializer to turn our QuerySets into
# binary string
from django.core.serializers import serialize
from .serializers import AppUserSerializer

# Json.loads will turn binary strings into JSON data
import json
class AllAppUsers(APIView):
    
    def get(self, request):
        app_users = AppUser.objects.order_by('first_name')
        app_users_serialized = serializer = AppUserSerializer(app_users)
        return Response(serializer.data)
    

class SelectAppUser(APIView):

    def get_app_user(self, id):

        if type(id) == int:
            return AppUser.objects.get(id = id)
        else:
            return AppUser.objects.get(first_name = id)

    def get(self, request, id):

        app_user = self.get_app_user(id)
        app_user_serialized = AppUserSerializer(app_user, many)
        return Response(app_user_serialized)
        


