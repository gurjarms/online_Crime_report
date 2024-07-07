from django import forms
from .models import Feedback_table
from .widget import datepicker


class temp(forms.Form):
    name = forms.CharField(max_length=50, required=False)


class Feedback_Form(forms.ModelForm):
    class Meta:
        model = Feedback_table
        fields = [
            'Full_Name', 'Email', 'Message'
        ]
        widgets = {
            'Message': forms.Textarea(attrs={'cols': 30, 'rows': 3})
        }
