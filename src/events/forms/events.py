from django import forms

from events.choices import VISIBILITY_CHOICES
from events.models import Event

class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=100, min_length=3, widget=forms.TextInput(attrs={'class':''}))
    location = forms.CharField(max_length=200, min_length=3, widget=forms.TextInput(attrs={'class':''}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class':''}))
    visibility = forms.CharField(max_length=10, widget=forms.Select(attrs={'class':''}, choices=VISIBILITY_CHOICES))
    start_time = forms.DateTimeField(input_formats = ['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_time = forms.DateTimeField(input_formats = ['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'))

    class Meta:
        model = Event
        fields = ('name', 'details', 'location', 'start_time', 'end_time', 'visibility')