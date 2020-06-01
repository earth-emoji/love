from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.decorators import members_required
from discussions.models import Topic, Entry
from discussions.serializers import EntrySerializer

@login_required
@members_required
@api_view(['GET', 'POST'])
def entry_collection(request, slug):
    try:
        topic = Topic.objects.get(slug=slug)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        entries = Entry.objects.filter(topic=topic).order_by('-created_at')
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'content': request.data.get('content'),
            'topic_pk': topic.pk,
            'author_pk': request.user.member.pk
        }
        serializer = EntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


