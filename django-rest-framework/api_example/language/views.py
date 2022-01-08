from django.shortcuts import render
from rest_framework import viewsets

# you can add permission in this views.py 
# or in settings.py 
from rest_framework import permissions

from .models import Paradigm, Language, Programmer
from .serializers import ParadigmSerializer, LanguageSerializer, ProgrammerSerializer

# Create your views here.
class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class LauguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    # permission_classes = (permissions.AllowAny, ) # default