from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.decorators import members_required
from discussions.models import Discussion, Topic
from discussions.forms import TopicForm, ConversationForm

@login_required
@members_required
def topic_create(request, slug):
    template_name = 'topics/form.html'
    context = {}

    if slug is None or slug == '':
        return redirect('not-found')

    discussion = Discussion.objects.get(slug=slug)

    if discussion is None:
        return redirect('not-found')

    if request.method == "POST":
        form = TopicForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.discussion = discussion
            c.moderator = request.user.member
            c.save()
            return redirect(c.get_absolute_url())
    form = TopicForm()

    context['discussion'] = discussion
    context['form'] = form

    return render(request, template_name, context)

@login_required
@members_required
def topic_details(request, slug):
    template_name = 'topics/details.html'
    context = {}

    if slug is None or slug == '':
        return redirect('not-found')

    topic = Topic.objects.get(slug=slug)

    if topic is None:
        return redirect('not-found')

    form = ConversationForm()

    context['topic'] = topic
    context['form'] = form

    return render(request, template_name, context)
