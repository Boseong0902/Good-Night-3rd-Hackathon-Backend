from rest_framework import generics
from ..models.comment_models import Comment
from ..serializers.comment_serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        wish_id = self.kwargs.get('wish_id')  # URL에서 소원의 ID를 가져옴
        serializer.save(wish_id=wish_id)  # 댓글을 저장할 때 해당 소원과 연결


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        wish_id = self.kwargs.get('wish_id')  # URL에서 소원의 ID를 가져옴
        return Comment.objects.filter(wish_id=wish_id, deleted_at__isnull=True).order_by('-created_at')
    

class CommentDeleteView(APIView):
    def delete(self, request, pk, format=None):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.deleted_at = timezone.now()  # Soft delete by setting deleted_at
            comment.save()
            return Response({"message": "Comment soft deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)