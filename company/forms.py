from django import forms
from .models import Vaccany

class DateField(forms.DateInput):
    input_type = 'date'


class VaccanyForm(forms.ModelForm):
    """Form definition for Vaccany."""

    class Meta:
        """Meta definition for Vaccanyform."""

        model = Vaccany
        exclude = ('user',)
        widgets = {
            'last_date': DateField(),
        }

