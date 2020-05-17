from django import forms

from campaigns.models import Campaign

class CampaignForm(forms.ModelForm):
    title = forms.CharField(max_length=128, min_length=2, strip=True, widget=forms.TextInput(
        attrs={'class ': ''}))
    description = forms.CharField(
        strip=True, widget=forms.Textarea(attrs={'class ': ''}))
    funds_needed = forms.DecimalField(max_digits=6, decimal_places=2, widget=forms.NumberInput(
        attrs={'class': ''}))
    funds_available = forms.DecimalField(max_digits=6, decimal_places=2, widget=forms.NumberInput(
        attrs={'class': ''}))

    class Meta:
        model = Campaign
        fields = [
            'title',
            'description',
            'funds_needed',
            'funds_available',
        ]