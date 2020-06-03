from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from discussions.models import Conversation

class ConversationForm(forms.ModelForm):
    title = forms.CharField(max_length=60, widget=forms.TextInput(attrs={}))
    content = SummernoteTextFormField(widget=SummernoteInplaceWidget())
    is_private = forms.BooleanField(widget=forms.CheckboxInput(attrs={}))

    class Meta:
        model = Conversation
        fields = ['title', 'content', 'is_private']
