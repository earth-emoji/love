from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from users.decorators import members_required
from campaigns.models import Volunteer, Campaign

@login_required
@members_required
def volunteer_response(request, slug):
    if slug is None or slug == "":
        return JsonResponse({'status':'false', 'message':"Results not found"}, status=404)

    volunteer = Volunteer.objects.get(slug=slug)

    if volunteer is None:
        return JsonResponse({'status':'false', 'message':"Results not found"}, status=404)

    if request.method == 'POST':
        status = request.POST['status']

        if status == "Accept":
            volunteer.status = status
            volunteer.save()
            campaign = volunteer.campaign
            campaign.volunteers_needed = campaign.volunteers_needed - 1
            campaign.save()

            data = {'success':True, 'message': f"{volunteer.member.user.name} has been added to {volunteer.campaign.title}"}
            return JsonResponse(data)
        elif status == "Reject":
            volunteer.delete()
            
            data = {'success':True, 'message': "Request has been removed"}
            return JsonResponse(data)

    return HttpResponse('')

@login_required
@members_required
def volunteer_request(request, slug):
    if slug is None or slug == "":
        return JsonResponse({'status':'false', 'message':"Results not found"}, status=404)

    campaign = Campaign.objects.get(slug=slug)

    if campaign is None:
        return JsonResponse({'status':'false', 'message':"Results not found"}, status=404)

    if request.method == 'POST':
        reason = request.POST['reason']

        Volunteer.objects.create(
            campaign=campaign, member=request.user.member, status="Pending", reason=reason)

        data = {'success':True, 'message': 'Your request has been sent!'}
        return JsonResponse(data)

    return HttpResponse('')
