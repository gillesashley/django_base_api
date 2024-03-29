from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    permission_classes: list = [IsAdminUser]
    queryset: object = get_user_model().objects.all()
    serializer_class: object = UserSerializer
