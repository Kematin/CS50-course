from django import forms

def get_pre_filed_content() -> str:
    return "content"

column_data = get_pre_filed_content()


class TextareaForm(forms.Form):
    textarea_form = forms.CharField(label="", widget=forms.Textarea(
        attrs=
            {
            'cols':80,
            'rows':20,
            'placeholder': '# Article name\n\nContent',
                }))


class TextareaFormPreFiled(forms.Form):
    textarea_form = forms.CharField(label="", widget=forms.Textarea(
        attrs=
            {
            'cols':80,
            'rows':20,
            'value': column_data,
                }))

