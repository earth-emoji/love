from django.utils import formats
from rest_framework import serializers

from accounts.models import Member
from discussions.models import Reply, Conversation

class ReplySerializer(serializers.ModelSerializer):
    author_pk = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source='author', write_only=True
    )
    conversation_pk = serializers.PrimaryKeyRelatedField(
        queryset=Conversation.objects.all(), source='conversation', write_only=True
    )
    serialized_date = serializers.SerializerMethodField()

    def get_serialized_date(self, obj):
        return formats.date_format(obj.created_at, 'DATETIME_FORMAT')

    class Meta:
        model = Reply
        fields = ('slug', 'content', 'created_at', 'serialized_date', 'conversation', 'conversation_pk', 'author', 'author_pk')
        depth = 2

class RepliesSerializer(serializers.ModelSerializer):
    author_pk = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source='author', write_only=True
    )
    parent_pk = serializers.PrimaryKeyRelatedField(
        queryset=Reply.objects.all(), source='parent', write_only=True
    )
    conversation_pk = serializers.PrimaryKeyRelatedField(
        queryset=Conversation.objects.all(), source='conversation', write_only=True
    )
    serialized_date = serializers.SerializerMethodField()

    def get_serialized_date(self, obj):
        return formats.date_format(obj.created_at, 'DATETIME_FORMAT')

    class Meta:
        model = Reply
        fields = ('slug', 'content', 'created_at', 'serialized_date', 'conversation', 'conversation_pk', 'author', 'author_pk', 'parent', 'parent_pk')
        depth = 2