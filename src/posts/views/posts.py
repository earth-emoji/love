from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.decorators import members_required
from campaigns.models import Campaign
from posts.forms import PostForm
from posts.models import Post
from posts.serializers import PostSerializer

@login_required
@members_required
def create_post(request, slug):
    template_name = 'posts/form.html'
    context = {}

    if slug is None or slug == "":
        return redirect('not-found')

    campaign = Campaign.objects.get(slug=slug)

    if campaign is None:
        return redirect('not-found')

    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.author = request.user.member
            c.campaign = campaign
            c.save()
            return redirect(campaign.get_absolute_url())
    else:
        form = PostForm()

    context["form"] = form
    context["campaign"] = campaign
    return render(request, template_name, context)

@login_required
@members_required
@api_view(['GET', 'POST'])
def post_collection(request, slug):
    try:
        campaign = Campaign.objects.get(slug=slug)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts = Post.objects.filter(campaign=campaign).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'campaign_pk': campaign.pk,
            'author_pk': request.user.member.pk
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


