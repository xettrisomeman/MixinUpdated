from rest_framework import viewsets

from .models import Name , Person
from .serializer import NameSerializer, PersonSerializer

class NameViewSet(viewsets.ModelViewSet):
    serializer_class = NameSerializer
    queryset = Name.objects.all()


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


