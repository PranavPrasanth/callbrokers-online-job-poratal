from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    """Form definition for Report."""

    class Meta:
        """Meta definition for Reportform."""

        model = Report
        exclude = ['work']
