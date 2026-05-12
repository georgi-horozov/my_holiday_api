from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from my_holiday.comment.api.serializers import CommentSerializer
from my_holiday.comment.models import Comment


class CommentViesSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(to_place__user = self.request.user)
    
    
    def perform_create(self, serializer):
        serializer.save(to_place__user = self.request.user)
