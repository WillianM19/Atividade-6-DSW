from django import forms
from .models import disc

class CreateDisc(forms.ModelForm):
    class Meta:
        model = disc
        fields = ['name', 'description', 'phonographicLabel', 'year', 'country', 'genre', 'amount', 'artist']    