# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class KsiazkiForm(ModelForm):

    class Meta:
        model = models.Ksiazki
        exclude = ('#','data')
        widgets = {'opis': Textarea(attrs={'rows': 2, 'cols': 80})}


"""KsiazkiFormSet = inlineformset_factory
    parent_model=models.Ksiazki,
    max_num=7,
    min_num=1,
    validate_max=True,
    validate_min=True,
    extra=2,
    fields=('tytul','autor')
)

"""
