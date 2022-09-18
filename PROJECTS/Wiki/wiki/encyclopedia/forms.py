from django import forms


class TextareaForm(forms.Form):
    textarea_form = forms.CharField(label="", widget=forms.Textarea(
        attrs=
            {
            'cols':80,
            'rows':20,
            'placeholder': '# Article name\n\nContent',
                }))

