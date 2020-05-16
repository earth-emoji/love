from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        strip=True, widget=forms.Textarea(attrs={'class ': ''}))
    is_published = forms.BooleanField()

    class Meta:
        model = Post
        fields = ['content', 'is_published']