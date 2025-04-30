__all__ = ['get_staff_list','get_staff','get_staff']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Staff
from core.serializers import StaffSerializer

@api_view(['GET'])
def get_staff_list(request):
    if request.method == 'GET':
        rides = Staff.objects.all()
        serializer = StaffSerializer(rides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_staff(request):
    if request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_staff(request,staff_slug):
    try:
        staff = Staff.objects.get(slug=staff_slug)
    except Staff.DoesNotExist:
        return Response({'error': 'Staff is not found'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
       serializer = StaffSerializer(staff)
       return Response(serializer.data, status=status.HTTP_200_OK)
