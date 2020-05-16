from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.decorators import members_required
from accounts.models import Member
from campaigns.models import Campaign
from posts.models import Post
from posts.serializers import PostSerializer

@login_required
@members_required
@api_view(['GET', 'POST'])
def post_collection(request, slug):
    try:
        campaign = Campaign.objects.get(slug=slug)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if not(campaign.initiator == request.user.member):
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        posts = Post.objects.filter(campaign=campaign).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'is_published': True,
            'campaign': campaign.pk,
            'author': request.user.member.pk
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


