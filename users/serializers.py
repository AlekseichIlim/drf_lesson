from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Расширяем стандартный сериализатор для получения пары токенов
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token
