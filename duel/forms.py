from django import forms

from .models import Post, Profile, Organisation


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-file-input'}),

        }


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['org']


class AddOrg(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['org_name', 'vote_type']
