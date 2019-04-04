from .models import Profile,Project,Post
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','profile']       



