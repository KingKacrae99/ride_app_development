__all__ = ['create_location','get_location_list','get_location']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Location
from core.serializers import LocationSerializer

@api_view(['POST'])
def create_location(request):
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_location_list(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_location(request, location_id):
    try:
        location = Location.Objects.get(id=location_id)
    except Location.DoesNotExist:
        return Response({'error': 'Request not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data,status=status.HTTP_200_OK)