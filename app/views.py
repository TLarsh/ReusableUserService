from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from .utils.response_handler import ResponseHandler
from .services.user_services import UserRegistrationServices
from rest_framework import status

class UserRegistrationAPIView(APIView):
    def post(self, requset, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=requset.data)
        if not serializer.is_valid():
            return ResponseHandler.error(
                message='Validation Failed',
                errors = serializer.errors
            )

        service = UserRegistrationServices(**serializer.validated_data)
        user, error = self.execute(service.register)

        if error:
            return ResponseHandler.error(
                message='Registration failed', errors=error, status_code=status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'id':user.id,
            'email':user.email,
            'name': f'{user.first_name} {user.last_name}',
            'role':user.role
        }
        return ResponseHandler.success(message='User registered successfully', data=data, status_code=status.HTTP_201_CREATED)
