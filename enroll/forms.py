from django import forms
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm
# model from class
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }