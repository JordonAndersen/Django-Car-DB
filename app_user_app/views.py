from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AppUser
from .serializers import AppUserSerializer

class AllAppUsers(APIView):
    
    def get(self, request):
        app_users = AppUser.objects.order_by('pk')
        serializer = AppUserSerializer(app_users, many=True)  
        return Response(serializer.data)
    
    def post(self, request, response):
        new_app_user = AppUser(**request.data)
        new_app_user.save()
        new_app_user.full_clean()
        new_app_user_serialized = AppUserSerializer(new_app_user_serialized, many=False)

class SelectAppUsers(APIView):

    def get_app_user(self, id):
        if isinstance(id, int):
            return AppUser.objects.get(id=id)
        else:
            return AppUser.objects.get(first_name=id.title())

    def get(self, request, id):
        app_user = self.get_app_user(id)
        app_user_serialized = AppUserSerializer(app_user, many=False)
        return Response(app_user_serialized.data)
    
    def delete(self, request, id):
        app_user = self.get_app_user(id)
        name = app_user.name
        app_user.delete()

        return Response(f'{name} was deleted')
