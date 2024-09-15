from uuid import uuid4

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from users.models import User


class UserCreateApi(APIView):

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=255)
        password = serializers.CharField(max_length=255)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        email = serializers.EmailField(max_length=255)

    def post(self, request: Request) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serialized_data: dict = serializer.data

        email: str = serialized_data['email']
        password: str = serialized_data['password']

        user = User(
            email=email,
            username=uuid4().hex,
            is_active=True,
        )
        user.set_password(password)
        user.save()
        serializer = self.OutputSerializer(user)
        return Response(serializer.data)
