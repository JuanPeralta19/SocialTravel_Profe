from django import forms
from SocialTravel.models import post

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'