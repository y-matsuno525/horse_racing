from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

class VoteForm(forms.Form):
    #choicesはタプルのリストじゃないとだめ
    def __init__(self,horses=None,*args,**kwargs):
        super(VoteForm, self).__init__(*args, **kwargs) #よくわからんけど必要
        self.fields['choice']=forms.ChoiceField(choices=[(horse.name,horse.name) for horse in horses],widget=forms.RadioSelect()) 
        