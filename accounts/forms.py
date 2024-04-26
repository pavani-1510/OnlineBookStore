from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'  # or specify the fields you want to include in the form
class TwoStepVerificationForm(forms.Form):
    verification_code = forms.CharField(label='Verification Code', max_length=6)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

from django import forms

class CCareForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
