from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import Member
from contacts.models import Contact, ContactGroup, Message
from users.decorators import members_required

@login_required
@members_required
def contact_list(request):
    template_name = 'contacts/contact_list.html'
    context = {}
    contact_groups = ContactGroup.objects.filter(creator=request.user.member, is_private=True)
    contacts = Contact.objects.filter(group__in=contact_groups.values_list('id', flat=True))

    context["contacts"] = contacts
    return render(request, template_name, context)