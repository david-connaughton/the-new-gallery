from django import forms
from .models import Tour


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('tour', 'date_preference', 'analogue_or_digital',
                  'skill_level', 'dietary_requirements', 'any_comments')
        