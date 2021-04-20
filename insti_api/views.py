from rest_framework import generics
from .serializers import UnivSerializers
from institutions.models import University


# Create your views here.
class UnivList(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UnivSerializers
