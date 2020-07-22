from django.utils import formats
from rest_framework import serializers

from accounts.models import Member
from campaigns.models import Campaign
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    author_pk = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source='author', write_only=True
    )
    campaign_pk = serializers.PrimaryKeyRelatedField(
        queryset=Campaign.objects.all(), source='campaign', write_only=True
    )
    serialized_date = serializers.SerializerMethodField()

    def get_serialized_date(self, obj):
        return formats.date_format(obj.created_at, 'DATETIME_FORMAT')

    class Meta:
        model = Post
        fields = ('slug', 'title', 'content', 'created_at', 'serialized_date', 'campaign', 'campaign_pk', 'author', 'author_pk')
        depth = 2