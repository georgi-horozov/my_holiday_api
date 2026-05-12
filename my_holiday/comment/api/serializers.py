from rest_framework import serializers

from my_holiday.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "date_time_of_publication"]