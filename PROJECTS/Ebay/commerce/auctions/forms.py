from django import forms
from .models import Listing, Commentary

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'cost', 'image_url', 'description', 'category_names',]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 8, 'cols': 40, 'style': 'resize: none;'}),
        }
        error_messages = {
            'cost': {'min_value': 'The value must be greater than or equal to 0.'}
        }

    cost = forms.FloatField(min_value=0.0)

class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['commentary']
