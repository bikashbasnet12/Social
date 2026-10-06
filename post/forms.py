from django import forms
from .models import post

class createpostform(forms.ModelForm):
    
    class Meta:
        model = post
        fields = ['content','image']