from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from discussions.models import Entry

class EntryForm(forms.Form):
    content = SummernoteTextFormField(widget=SummernoteInplaceWidget())
