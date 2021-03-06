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
    przedmiot = models.CharField(verbose_name='Przedmiot', max_length=30)
    autor = models.CharField(verbose_name='Autor', max_length=30)
    wydawnictwo = models.CharField(verbose_name='Wydawnictwo', max_length=30)
    kontakt = models.CharField(verbose_name='Kontakt', max_length=30)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    opis = models.CharField(verbose_name='Opis Ksiazki', max_length=30)
    data = models.DateField('dodano', auto_now_add=True)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % (self.tytul)

    class Meta:
        verbose_name_plural = 'ksiazki'
