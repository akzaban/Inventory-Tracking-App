from django import forms
from .models import Details
 
class detailsform(forms.ModelForm):
    class Meta:
        model=Details
        fields="__all__"
