__all__ = ['create_booking', 'get_booking_list', 'get_booking']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Booking
from core.serializers import BookingSerializer

@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_booking_list(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_200_OK)
