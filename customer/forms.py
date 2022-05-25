from django import forms
from .models import Work, Feedback

class WorkForm(forms.ModelForm):
    """Form definition for Work."""

    class Meta:
        """Meta definition for Workform."""

        model = Work
        exclude = ('user',)

class FeedbackForm(forms.ModelForm):
    """Form definition for Feedback."""

    class Meta:
        """Meta definition for Feedbackform."""

        model = Feedback
        exclude = ('user','status')