from rest_framework import generics
from ..models.wish_models import Wish
from ..serializers.wish_serializers import WishSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class WishCreateView(generics.CreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class WishDeleteView(APIView):
    def delete(self, pk):
        try:
            wish = Wish.objects.get(pk=pk)
            wish.deleted_at = timezone.now()
            wish.save()
            return Response({"message": "Wish soft deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Wish.DoesNotExist:
            return Response({"error": "Wish not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
class WishConfirmView(APIView):
    def post(self, request, pk):
        try:
            wish = Wish.objects.get(pk=pk, is_confirm='pending')
            status = request.data.get('status')
            if status not in ['approved', 'rejected']:
                return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
            wish.is_confirm = status
            wish.save()
            return Response({"message": f"Wish {status} successfully"}, status=status.HTTP_200_OK)
        except Wish.DoesNotExist:
            return Response({"error": "Pending wish not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
class WishDetailView(generics.RetrieveAPIView):
    queryset = Wish.objects.filter(is_confirm='approved', deleted_at__isnull=True)
    serializer_class = WishSerializer


class WishListView(generics.ListAPIView):
    queryset = Wish.objects.filter(deleted_at__isnull=True).order_by('-created_at')
    serializer_class = WishSerializer


class WishListView(generics.ListAPIView):
    queryset = Wish.objects.filter(deleted_at__isnull=True).order_by('-created_at')
    serializer_class = WishSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'is_confirm']
    search_fields = ['title', 'content']