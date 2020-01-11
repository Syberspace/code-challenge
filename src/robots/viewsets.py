from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import *
from .models import *

class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class DanceoffViewSet(viewsets.ModelViewSet):
    queryset = Danceoff.objects.all()
    serializer_class = DanceoffSerializer


class BattleViewSet(viewsets.ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
