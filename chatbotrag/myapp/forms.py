# myapp/forms.py
from django import forms

DOMAIN_CHOICES = [
    ('Education', 'Education'),
    ('Legal', 'Legal'),
    ('Finance', 'Finance'),
    ('Real Estate', 'Real Estate'),
    ('News & Media', 'News & Media'),
    ('Others', 'Others'),
]

class DatasetForm(forms.Form):
    domain = forms.ChoiceField(choices=DOMAIN_CHOICES, label="Select Domain")
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), label="Select Files")
    name = forms.CharField(max_length=100, label="Name")
