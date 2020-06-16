from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from rest_framework.generics import ListAPIView

from accounts.models import Member
from campaigns.models import Campaign
from users.decorators import members_required

from events.forms import EventForm
from events.models import Event
from events.serializers import EventSerializer
from events.pagination import StandardResultsSetPagination

@login_required
@members_required
def public_events(request):
    template_name = 'events/public_events.html'
    context = {}

    events = Event.objects.filter(visibility='Public')
    context['events'] = events
    return render(request, template_name, context)

@login_required
@members_required
def create_events(request):
    template_name = "events/form.html"
    context = {}
    if request.method == "POST":
        form = EventForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            # 2020-06-04 14:26
            # c.start_time = datetime.fromtimestamp(form.cleaned_data['start_time'])
            # c.end_time = datetime.strptime(form.cleaned_data['end_time'])
            c.creator = request.user.member
            c.save()
            return redirect('events:user-events')
    else:
        form = EventForm()
    context["form"] = form
    return render(request, template_name, context)

@login_required
@members_required
def user_events(request):
    template_name = 'events/user_events.html'
    context = {}
    events = Event.objects.filter(creator=request.user.member).order_by('-created_at')
    context["events"] = events
    return render(request, template_name, context)

class EventListing(ListAPIView):
    # set the pagination and serializer class

    pagination_class = StandardResultsSetPagination
    serializer_class = EventSerializer

    def get_queryset(self):
        # filter the queryset based on the filters applied

        query_list = Event.objects.filter(creator=self.request.user.member).order_by("-start_time")

        visibility = self.request.query_params.get('visibility', None)
        event_day = self.request.query_params.get('day', None)
        sort_by = self.request.query_params.get('sort_by', None)

        if visibility:
            query_list = query_list.filter(visibility=visibility).order_by("name")
        if event_day:
            query_list = query_list.filter(start_time__day=event_day).order_by("-start_time")

        if sort_by == "name":
            query_list = query_list.order_by("name")
        elif sort_by == "start_time":
            query_list = query_list.order_by("-start_time")
        return query_list

def get_visibility(request):
    if request.method == "GET" and request.is_ajax():
        events = Event.objects.filter(creator=request.user.member).exclude(visibility__exact='').order_by('-start_time').distinct()
        data = {
            "events": events,
        }
        return JsonResponse(data, status=200)

def get_event_day(request):
    if request.method == "GET" and request.is_ajax():
        events = Event.objects.filter(creator=request.user.member).exclude(start_time__date__lt=date.today()).order_by('-start_time').distinct()
        data = {
            "events": events,
        }
        return JsonResponse(data, status=200)

@login_required
@members_required
def attend_event(request):
    if request.method == "POST" and request.is_ajax():
        event = Event.objects.get(slug=request.POST['slug'])
        event.attendees.add(request.user.member)
        data = {'success':True, 'message': "You have been added to the event."}
        return JsonResponse(data, status=200)
    return HttpResponse("")