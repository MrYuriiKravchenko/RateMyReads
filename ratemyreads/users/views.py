from rest_framework import viewsets
from .models import User
from users.serializers import UserSerializer
from rest_framework.response import Response

class UserViewsSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User.objects.all()