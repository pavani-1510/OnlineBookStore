from django import forms
class PaymentForm(forms.Form):
    transid = forms.NumberInput()

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']