from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import Member
from users.decorators import members_required
from campaigns.models import Team, Campaign, Volunteer
from campaigns.serializers import TeamSerializer

@login_required
@members_required
def campaign_teams(request, slug):
    template_name = 'teams/index.html'
    context = {}

    if slug is None or slug == "":
        return redirect('not-found')

    campaign = Campaign.objects.get(slug=slug)

    if campaign is None:
        return redirect('not-found')

    context["campaign"] = campaign

    return render(request, template_name, context)

@login_required
@members_required
def create_team(request):
    if request.method == 'POST':
        slug = request.POST['slug']
        name = request.POST['name']

        campaign = Campaign.objects.get(slug=slug)

        Team.objects.create(name=name, campaign=campaign)

        data = {'success':True, 'message': 'Team was created!'}
        return JsonResponse(data)

    return HttpResponse('')

@login_required
@members_required
def team_details(request, slug):
    template_name = 'teams/details.html'
    context = {}

    if slug is None or slug == "":
        return redirect('not-found')

    team = Team.objects.get(slug=slug)

    if team is None:
        return redirect('not-found')

    volunteers = Volunteer.objects.filter(campaign=team.campaign, status="Accept").exclude(member_id__in=team.members.all())

#     blocked_delivery_times = BlockedDeliveryTime.objects.filter(delivery_date=delivery_date) \
#     .values('delivery‌​_time')
# delivery_times = DeliveryTime.objects.exclude(id__in=blocked_delivery_times)

    context["team"] = team
    context["volunteers"] = volunteers

    return render(request, template_name, context)

@login_required
@members_required
def make_team_leader(request, team_slug, leader_slug):
    if team_slug is None or team_slug == "":
        return redirect('not-found')

    if leader_slug is None or leader_slug == "":
        return redirect('not-found')

    team = Team.objects.get(slug=team_slug)
    leader = Member.objects.get(slug=leader_slug)

    if team is None or leader is None:
        return redirect('not-found')

    team.leader = leader
    team.save()

    return redirect('teams:details', team.slug)

@login_required
@members_required
def make_team_member(request, team_slug, member_slug):
    if team_slug is None or team_slug == "":
        return redirect('not-found')

    if member_slug is None or member_slug == "":
        return redirect('not-found')

    team = Team.objects.get(slug=team_slug)
    member = Member.objects.get(slug=member_slug)

    if team is None or member is None:
        return redirect('not-found')

    team.members.add(member)

    return redirect('teams:details', team.slug)

@login_required
@members_required
@api_view(['GET'])
def team_collection(request, slug):
    try:
        campaign = Campaign.objects.get(slug=slug)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if not(campaign.initiator == request.user.member):
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        teams = Team.objects.filter(campaign=campaign)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
