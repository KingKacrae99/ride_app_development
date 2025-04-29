__all__ = []

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