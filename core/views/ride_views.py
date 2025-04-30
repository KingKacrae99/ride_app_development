__all__ = ['create_ride', 'get_ride_list', 'get_ride_by_id']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Ride
from core.serializers import RideSerializer

@api_view(['POST'])
def create_ride(request):
    serializer = RideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_ride_list(request):
    rides = Ride.objects.all()
    serializer = RideSerializer(rides, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_ride_by_id(request, ride_id):
    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Response({'error': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = RideSerializer(ride)
    return Response(serializer.data, status=status.HTTP_200_OK)
