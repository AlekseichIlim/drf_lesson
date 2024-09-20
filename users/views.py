from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """Получение JWT-токена"""
    serializer_class = MyTokenObtainPairSerializer
