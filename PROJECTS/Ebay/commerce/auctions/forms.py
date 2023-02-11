from django import forms
from .models import Listing, Commentary

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'description', 'cost', 'category_names', 'image_url']

class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['commentary']
