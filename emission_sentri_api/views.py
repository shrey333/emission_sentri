from rest_framework import generics
from .models import Emissions
from .serializers import EmissionsSerializer


class EmissionsList(generics.ListCreateAPIView):
    queryset = Emissions.objects.all()
    serializer_class = EmissionsSerializer
