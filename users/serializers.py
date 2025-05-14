from users.models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'profile_picture', 'bio', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}  
        read_only_fields = ['id']
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login with debugging.
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Validates the provided email and password with detailed error information.
        """
        email = data.get('email')
        password = data.get('password')
        
        # Try to authenticate
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
            
        if not user.is_active:
            raise serializers.ValidationError("User account is inactive")
        return user