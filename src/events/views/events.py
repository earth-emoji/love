from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.generics import ListAPIView

from accounts.models import Member
from campaigns.models import Campaign
from users.decorators import members_required

from events.forms import EventForm
from events.models import Event
from events.serializers import EventSerializer
from events.pagination import StandardResultsSetPagination


class EventListing(ListAPIView):
    # set the pagination and serializer class

    pagination_class = StandardResultsSetPagination
    serializer_class = EventSerializer

    def get_queryset(self):
        # filter the queryset based on the filters applied
        campaign = Campaign.objects.get(slug=self.request.query_params.get('campaign', None))

        query_list = Event.objects.filter(campaign=campaign).order_by("-start_time")

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

def get_visibility(request, slug):
    campaign = Campaign.objects.get(slug=slug)
    if request.method == "GET" and request.is_ajax():
        events = Event.objects.filter(campaign=campaign).exclude(visibility__exact='').order_by('-start_time').distinct()
        data = {
            "events": events,
        }
        return JsonResponse(data, status=200)

def get_event_day(request, slug):
    campaign = Campaign.objects.get(slug=slug)
    if request.method == "GET" and request.is_ajax():
        events = Event.objects.filter(campaign=campaign).exclude(start_time__date__lt=date.today()).order_by('-start_time').distinct()
        data = {
            "events": events,
        }
        return JsonResponse(data, status=200)