__all__ = ['get_student_list', 'get_student', 'create_student']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Student
from core.serializers import StudentSerializer

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_student(request, std_slug):
    try:
        student = Student.objects.get(slug=std_slug)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)
