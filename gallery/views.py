# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from .serializers import SymbolSerializer
from .models import Symbol

# Create your views here.


class SymbolViewSet(viewsets.ModelViewSet):
    serializer_class = SymbolSerializer
    queryset = Symbol.objects.all()
