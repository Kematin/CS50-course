from django import forms

# text
class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')


# checkbox
class CheckBoxForm(forms.Form):
    checkbox = forms.BooleanField(label="CheckBox")


# yes or no
class NoolForm(forms.Form):
    bool_form = forms.NullBooleanField(label="Yes or no")


# email form
class EmailForm(forms.Form):
    email = forms.EmailField(label='Email')


# url field
class UrlForm(forms.Form):
    url = forms.URLField(label='Url')


# etc in metani
# https://metanit.com/python/django/4.2.php
