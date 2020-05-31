from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from users.decorators import members_required
from accounts.models import Member
from campaigns.models import Campaign

@login_required
@members_required
def member_index(request):
    template_name = 'members/index.html'
    context = {}
    member = request.user.member

    campaigns = Campaign.objects.filter(initiator=member)[:5]

    context["campaigns"] = campaigns
    context["member"] = member

    return render(request, template_name, context)

@login_required
@members_required
def initiator_campaign_list(request):
    template_name = "campaigns/initiator_list.html"
    context = {}
    member = request.user.member

    campaigns = Campaign.objects.filter(initiator=member)
    
    context["campaigns"] = campaigns
    context["member"] = member
    return render(request, template_name, context)

@login_required
@members_required
def public_campaign_list(request, slug):
    template_name = "campaigns/public_list.html"
    context = {}

    if slug is None:
        return redirect('not-found')
    
    member = Member.objects.get(slug=slug)

    if member is None:
        return redirect('not-found')

    campaigns = Campaign.objects.filter(initiator=member)
    context["campaigns"] = campaigns
    context["member"] = member
    return render(request, template_name, context)