# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from gallery.serializers import SymbolSerializer
from .models import User, Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ('id', 'name',)


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    symbol = SymbolSerializer()

    class Meta:
        model = Vote

        fields = ('id', 'user', 'symbol', 'created',)
