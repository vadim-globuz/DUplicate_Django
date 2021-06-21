from django import forms

from .models import Post, Organisation


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-file-input'}),

        }


class OrgForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['users', 'organisation_name']
        widgets = {
            'users': forms.SelectMultiple(),
            'organisation_name': forms.TextInput()
        }
