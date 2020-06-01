from django.utils import formats
from rest_framework import serializers

from accounts.models import Member
from discussions.models import Entry, Topic

class EntrySerializer(serializers.ModelSerializer):
    author_pk = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source='author', write_only=True
    )
    topic_pk = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(), source='topic', write_only=True
    )
    serialized_date = serializers.SerializerMethodField()

    def get_serialized_date(self, obj):
        return formats.date_format(obj.created_at, 'DATETIME_FORMAT')

    class Meta:
        model = Entry
        fields = ('slug', 'content', 'created_at', 'serialized_date', 'topic', 'topic_pk', 'author', 'author_pk')
        depth = 2