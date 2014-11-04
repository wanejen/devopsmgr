__author__ = 'seiou'
from django import forms

class f_serverlist(forms.Form):
    id = forms.CharField(max_length=4)
    name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=10)
    opentime = forms.DateTimeField()
    type = forms.MultiValueField()