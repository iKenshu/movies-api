from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserRegisterSerializer, TokenObtainPairSerializer


class RegisterUserView(CreateAPIView):
    serializer_class = UserRegisterSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
