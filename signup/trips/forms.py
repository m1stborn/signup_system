from django import forms
from jsignature.forms import JSignatureField
class VisitorForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
    Company = forms.CharField(label='Company', max_length=100)
    Purpose = forms.CharField(label='Company', max_length=100)



class SignatureForm(forms.Form):
    signature = JSignatureField()