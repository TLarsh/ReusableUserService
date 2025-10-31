from rest_framework import serializers
from django.contrib.auth import get_user_model
from .services.user_services import UserRegistrationServices
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
        ]
    
    def validate_email(self, value):
        if User.objects.filter(email=value.lower().strip()).exist():
            raise serializers.ValidationError(
                'A user with this email already exist'
            )
        return value.lower().strip()
    
    def create(self, validated_data):
        services = UserRegistrationServices(**validated_data)
        user = services.register()

        return user