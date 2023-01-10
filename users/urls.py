from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterUserView, TokenObtainPairView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
]
