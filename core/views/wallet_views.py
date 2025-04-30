__all__ = ['get_student_list', 'get_student', 'create_student']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Wallet
from core.serializers import WalletSerializer

@api_view(['POST'])
def create_wallet(request):
    serializer = WalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_wallet_list(request):
    wallets = Wallet.objects.all()
    serializer = WalletSerializer(wallets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_wallet(request, std_slug):
    try:
        wallet = Wallet.objects.get(slug=std_slug)
    except Wallet.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = WalletSerializer(wallet)
    return Response(serializer.data, status=status.HTTP_200_OK)
