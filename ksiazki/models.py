# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Ksiazki(models.Model):
    UZYWANA = 'U'
    NOWA = 'N'
    STAN = ((UZYWANA, 'Używana'), (NOWA, 'Nowa'),)


    stan = models.CharField(max_length=1, choices=STAN, default=UZYWANA)
    tytul = models.CharField(verbose_name='Tytuł', max_length=30)
    przedmiot = models.TextField(blank=True, help_text='Przedmiot')
    autor = models.TextField(blank=True, help_text='Autor')
    wydawnictwo = models.TextField(blank=True, help_text='Wydawnictwo')
    kontakt = models.TextField(blank=True, help_text='Kontakt')
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    opis = models.TextField(blank=True, help_text='Opis Ksiazki')
    data = models.DateField('dodano', auto_now_add=True)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % (self.tytul)

    class Meta:
        verbose_name_plural = 'ksiazki'
