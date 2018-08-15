# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from gallery.models import Symbol


class User(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Vote(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )
    symbol = models.ForeignKey(to=Symbol)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{user}:{symbol}".format(
            user=self.user.name,
            symbol=self.symbol.name
        )
