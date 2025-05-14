from users.models import CustomUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from users.serializers import UserLoginSerializer, UserSerializer
from rest_framework.response import Response

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        """
        Customize permissions based on the action.
        """
        if self.action in ['create', 'retrieve', 'login_user']:
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        """
        Custom create method to handle user registration with additional validation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        
        return Response({
            'user': UserSerializer(user).data,
            'message': 'User created successfully'
        }, status=status.HTTP_201_CREATED)
        
    def destroy(self, request, *args, **kwargs):
        """
        Override destroy method to only allow users to delete their own account,
        or admin users to delete any account.
        """
        user_to_delete = self.get_object()
        current_user = request.user
        
        if user_to_delete.id == current_user.id or current_user.is_staff:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(
                {"error": "You don't have permission to delete this user account."},
                status=status.HTTP_403_FORBIDDEN
            )

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated], )
    def change_password(self, request):
        """
        Custom action to change user password.
        """
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not user.check_password(old_password):
            return Response({
                'error': 'Incorrect old password'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()
        
        return Response({
            'message': 'Password changed successfully'
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        """
        Handle user profile operations:
        - GET: Retrieve the current user's profile information
        - PUT/PATCH: Update the current user's profile information
        """
        user = request.user
        
        if request.method == 'GET':
            # View profile
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        
        elif request.method in ['PUT', 'PATCH']:
            # Update profile
            partial = request.method == 'PATCH'
            serializer = self.get_serializer(user, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            return Response({
                'user': serializer.data,
                'message': 'Profile updated successfully'
            })
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='login')
    def login_user(self, request):
        """
        Custom action for user login 
        """
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data
            
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'status': 'success',
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
                'user': {
                    'id': user.id,
                    'email': user.email
                }
            })
            
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    
'''class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data  
        refresh = RefreshToken.for_user(user)
        return Response({
            'status': 'success',
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            'user': {
                'id': user.id,
                'email': user.email
            }
        }, status=status.HTTP_200_OK)'''
