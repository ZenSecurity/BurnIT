# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, mixins
from .serializers import UserSerializer, VoteSerializer
from .models import User, Vote

# Create your views here.


class UserViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PollViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
