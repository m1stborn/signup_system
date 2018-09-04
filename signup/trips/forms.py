from django import forms
class VisitorForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
    Company = forms.CharField(label='Company', max_length=100)
    Purpose = forms.CharField(label='Company', max_length=100)

