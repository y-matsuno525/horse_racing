from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

class vote(forms.Form):
    def __init__(self,horses,*args,**kwargs):
        choice=forms.choiceField(label="radio",choices=horses,widget=forms.RadioSelect())