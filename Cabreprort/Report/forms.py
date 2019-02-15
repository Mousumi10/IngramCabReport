from django import forms
from Report.choices import *

class NameForm(forms.Form):
    office_location = forms.ChoiceField(choices = OFFICE_CHOICES, label="Office Location", initial='',
                               widget=forms.Select(),
                               required=True)
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
    your_name = forms.CharField(label='Your name')
