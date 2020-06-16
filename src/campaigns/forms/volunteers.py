from django import forms

from campaigns.models import Volunteer

class VolunteerForm(forms.ModelForm):
    reason = forms.CharField(
        strip=True, widget=forms.Textarea(attrs={'class ': ''}))

    class Meta:
        model = Volunteer
        fields = ['reason']