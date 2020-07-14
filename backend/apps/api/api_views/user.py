from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.contrib.auth import get_user_model
from apps.mainsite.app_models.users import User
from apps.api.serializers.user import UserSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def user_list(request):
    if request.method == 'GET':
        _user = get_user_model()
        data = _user.objects.all()
        serializer = UserSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def user_detail(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(UserSerializer(user, context={'request': request}).data)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status.HTTP_400_BAD_REQUEST)