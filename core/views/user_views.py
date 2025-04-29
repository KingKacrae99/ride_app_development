from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import CustomUser
from core.serializers import CustomUserSerializer

@api_view(['GET','POST'])
def get_user_list(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

__all__ = ['get_user_list', 'create_user']