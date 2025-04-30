__all__ = ['create_payment', 'get_payment_list', 'get_payment']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Payment
from core.serializers import PaymentSerializer

@api_view(['POST'])
def create_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_payment_list(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_payment(request, payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PaymentSerializer(payment)
    return Response(serializer.data, status=status.HTTP_200_OK)
