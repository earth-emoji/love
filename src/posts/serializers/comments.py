from django.utils import formats
from rest_framework import serializers

from accounts.models import Member
from posts.models import Comment, Post

class CommentSerializer(serializers.ModelSerializer):
    author_pk = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source='author', write_only=True
    )
    post_pk = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source='post', write_only=True
    )
    serialized_date = serializers.SerializerMethodField()

    def get_serialized_date(self, obj):
        return formats.date_format(obj.created_at, 'DATETIME_FORMAT')

    class Meta:
        model = Comment
        fields = ('content', 'created_at', 'serialized_date', 'post', 'post_pk', 'author', 'author_pk')
        depth = 2
