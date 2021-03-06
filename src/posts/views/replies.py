from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework import status

from users.decorators import members_required
from posts.models import Post, Reply
from posts.serializers import RepliesSerializer, ReplySerializer

@login_required
@members_required
@api_view(['GET', 'POST'])
def reply_collection(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return JsonResponse({'message': 'Record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        replies = Reply.objects.filter(post=post).order_by('-created_at')
        serializer = ReplySerializer(replies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = {
            'content': request.data.get('c-content'),
            'post_pk': post.pk,
            'author_pk': request.user.member.pk
        }
        serializer = ReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@members_required
@api_view(['GET', 'POST'])
def replies_collection(request, slug):
    try:
        reply = Reply.objects.get(slug=slug)
    except Reply.DoesNotExist:
        return JsonResponse({'message': 'Record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        replies = Reply.objects.filter(parent=reply).order_by('-created_at')
        serializer = RepliesSerializer(replies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = {
            'content': request.data.get('reply-content'),
            'post_pk': reply.post.pk,
            'author_pk': request.user.member.pk,
            'parent_pk': reply.pk,
        }
        serializer = RepliesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)