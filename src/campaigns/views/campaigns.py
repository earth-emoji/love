from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.decorators import members_required

from campaigns.forms import CampaignForm
from campaigns.models import Campaign, Volunteer
from discussions.models import Discussion, Topic, Conversation
from events.models import Event

@login_required
@members_required
def campaign_list(request):
    template_name = 'campaigns/public_list.html'
    context = {}

    campaigns = Campaign.objects.all()
    context["campaigns"] = campaigns

    return render(request, template_name, context)

@login_required
@members_required
def campaign_create(request):
    template_name = "campaigns/create.html"
    context = {}
    form = CampaignForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.initiator = request.user.member
        obj.save()
        topic = Topic.objects.create(campaign=obj, name=f"{obj.title} Topic", description=f"{obj.title} Conversations")
        Conversation.objects.create(title=f"Welcome to the {obj.title} campaign", content=form.cleaned_data['opener'], topic=topic, author=obj.initiator)
        return redirect('campaigns:idetails', obj.slug)
    context["form"] = form
    return render(request, template_name, context)

@login_required
@members_required
def campaign_details(request, slug):
    template_name = "campaigns/public_details.html"
    context = {}

    if slug is None or slug == "":
        return redirect('not-found')

    campaign = Campaign.objects.get(slug=slug)

    if campaign is None:
        return redirect('not-found')

    volunteers = Volunteer.objects.filter(campaign=campaign, status="Accepted")
    
    context["campaign"] = campaign
    context["volunteers"] = volunteers
    
    return render(request, template_name, context)

@login_required
@members_required
def initiator_campaign_details(request, slug):
    template_name = "campaigns/initiator_details.html"
    context = {}

    if slug is None or slug == "":
        return redirect('not-found')

    campaign = Campaign.objects.get(slug=slug)

    if campaign is None:
        return redirect('not-found')

    if not (campaign.initiator == request.user.member):
        return redirect('forbidden')

    volunteer_requests = Volunteer.objects.filter(campaign=campaign, status="Pending")[:5]

    volunteers = Volunteer.objects.filter(campaign=campaign, status="Accepted")

    context["campaign"] = campaign
    context["volunteers"] = volunteers
    context["volunteer_requests"] = volunteer_requests

    return render(request, template_name, context)

@login_required
@members_required
def campaign_edit(request, slug):
    template_name = "campaigns/edit.html"
    context = {}

    if slug is None:
        return redirect('not-found')

    campaign = Campaign.objects.get(slug=slug)

    if campaign is None:
        return redirect('not-found')

    if not (campaign.initiator == request.user.member):
        return redirect('forbidden')
    
    form = CampaignForm(request.POST or None, instance=campaign)

    if form.is_valid():
        form.save()
        redirect('campaigns:ilist')

    context["campaign"] = campaign
    context["form"] = form

    return render(request, template_name, context)

@login_required
@members_required
def campaign_delete(request, slug):
    template_name = "campaigns/delete.html"
    context = {}

    if slug is None:
        return redirect('not-found')

    campaign = Campaign.objects.get(slug=slug)

    if campaign is None:
        return redirect('not-found')

    if not (campaign.initiator == request.user.member):
        return redirect('forbidden')
    
    if request.method == 'POST':
        campaign.delete()
        redirect('campaigns:ilist', request.user.member.slug)
    context["campaign"] = campaign

    return render(request, template_name, context)
