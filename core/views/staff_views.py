__all__ = ['get_staff_list', 'get_staff', 'create_staff']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Staff
from core.serializers import StaffSerializer

@api_view(['GET'])
def get_staff_list(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_staff(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_staff(request, staff_slug):
    try:
        staff = Staff.objects.get(slug=staff_slug)
    except Staff.DoesNotExist:
        return Response({'error': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = StaffSerializer(staff)
    return Response(serializer.data, status=status.HTTP_200_OK)
