from django.utils import formats
from rest_framework import serializers

from accounts.models import Member
from campaigns.models import Campaign
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    creator_pk = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source='creator', write_only=True
    )
    serialized_date = serializers.SerializerMethodField()

    def get_serialized_date(self, obj):
        return formats.date_format(obj.created_at, 'DATETIME_FORMAT')

    class Meta:
        model = Event
        fields = (
            'slug',
            'name',
            'details',
            'location',
            'start_time',
            'end_time',
            'visibility',
            'created_at',
            'serialized_date',
            'creator',
            'creator_pk'
        )
        depth = 2