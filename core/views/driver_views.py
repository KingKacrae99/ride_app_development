__all__ = ['create_driver','get_driver_list','get_driver']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Driver
from core.serializers import DriverSerializer

@api_view(['POST'])
def create_driver(request):
    if request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_driver_list(request):
    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_driver(request, driver_id):
    try:
        driver = Driver.Objects.get(id=driver_id)
    except Driver.DoesNotExist:
        return Response({'error': 'Request not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DriverSerializer(driver)
        return Response(serializer.data,status=status.HTTP_200_OK)