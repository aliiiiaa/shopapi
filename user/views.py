import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserLoginSerializer, UserCreateSerializer
from django.contrib.auth.models import User


@api_view(['POST'])
def authorization_api_view(request):
    """validate data"""
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    """ get user data"""
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    """authenticate"""
    user = authenticate(**serializer.validated_data)

    if user:
        """send token"""
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})

    else:
        """authenticate error"""
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'error': 'user does not exist'})


@api_view(['POST'])
def registration_api_view(request):
    """validated data"""
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    """create user"""
    user = User.objects.create_user(**serializer.validated_data)
    code = UserCreateSerializer.code

    return Response(data={'user_id': user.id, 'code': code})


@api_view(['POST'])
def confirm_api_view(request):
    """confirm user registrations"""
    code = request.data.get('code')
    if code == UserCreateSerializer.code:
        UserCreateSerializer.is_active = True