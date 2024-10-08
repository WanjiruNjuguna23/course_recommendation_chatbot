# forms.py

from django import forms
from .models import Interest

# Form that allows users to select multiple interests
class InterstForm(forms.Form):
    interests = forms.ModelMultipleChoiceField(
        queryset = Interest.objects.all(),  # Fetch all available interests from the database
        widget = forms.CheckboxSelectMultiple,  # Render interests as checkboxes
        required=True  # This field is required
    )
