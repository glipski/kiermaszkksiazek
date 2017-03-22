# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class KsiazkiForm(ModelForm):

    class Meta:
        model = models.Ksiazki
        exclude = ('#','data')
        widgets = {'opis': Textarea(attrs={'rows': 1, 'cols': 50}),
                  'tytul': Textarea(attrs={'rows': 1, 'cols': 50}),
                  'przedmiot': Textarea(attrs={'rows': 1, 'cols': 50}),
                  'wydawnictwo': Textarea(attrs={'rows': 1, 'cols': 50}),
                  'kontakt': Textarea(attrs={'rows': 1, 'cols': 50}),
                  'cena': Textarea(attrs={'rows': 1, 'cols': 50}),
                  'opis': Textarea(attrs={'rows': 1, 'cols': 50}),
                  'data': Textarea(attrs={'rows': 1, 'cols': 50}),
                  'uzytkownik': Textarea(attrs={'rows': 1, 'cols': 50})}
