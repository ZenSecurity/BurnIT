# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import Symbol


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol

        fields = ('id', 'name', 'description', 'public', 'image',)
        read_only_fields = ('name', 'description', 'public', 'image',)
