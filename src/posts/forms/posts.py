from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from posts.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=60, widget=forms.TextInput(attrs={}))
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ['title', 'content']
