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
        read_only_fields = ('id', 'created',)
        write_only_fields =  ('user', 'symbol',)

    def create(self, validated_data):
        print(validated_data)
        #user_data = validated_data.pop('user')
