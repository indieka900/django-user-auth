from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet as Users

router = DefaultRouter()
router.register('users', Users, basename="User views")

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', LoginView.as_view(), name='user_login'),
]