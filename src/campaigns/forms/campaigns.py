from django import forms

from campaigns.models import Campaign
from classifications.fields import GroupedModelChoiceField
from classifications.models import Cause

class CampaignForm(forms.ModelForm):
    title = forms.CharField(max_length=128, min_length=2, strip=True, widget=forms.TextInput(
        attrs={'class ': ''}))
    description = forms.CharField(
        strip=True, widget=forms.Textarea(attrs={'class ': ''}))
    opener = forms.CharField(
        strip=True, widget=forms.Textarea(attrs={'class ': ''}))
    funds_needed = forms.DecimalField(max_digits=11, decimal_places=2, widget=forms.NumberInput(
        attrs={'class': ''}))
    funds_available = forms.DecimalField(max_digits=11, decimal_places=2, widget=forms.NumberInput(
        attrs={'class': ''}))
    cause = GroupedModelChoiceField(
        queryset=Cause.objects.all(),
        choices_groupby='classification'
    )
    volunteers_needed = forms.IntegerField(max_value=100, widget=forms.NumberInput(attrs={'class': ''}))

    class Meta:
        model = Campaign
        fields = [
            'title',
            'description',
            'funds_needed',
            'funds_available',
            'cause',
            'volunteers_needed',
            'opener',
        ]