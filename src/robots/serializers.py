from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import *


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['id', 'name', 'powermove',
                  'experience', 'out_of_order', 'avatar']


class DanceoffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Danceoff
        fields = ['id', 'battles']

    def validate(self, data):
        if len(data['battles']) != 5:
            raise ValidationError('A Danceoff needs exactly 5 battles')

        pairings = [(x.r1, x.r2) for x in data['battles']]
        team1 = [x.r1 for x in data['battles']]
        team2 = [x.r2 for x in data['battles']]
        if len(pairings) != len(set(pairings)):
            raise ValidationError(
                'Each pair of robots is only allowed to dance once')

        if len(team1) != len(set(team1)) or len(team2) != len(set(team2)):
            raise ValidationError('Teams do not have 5 Members')

        if len(team1+team2) != len(set(team1+team2)):
            raise ValidationError('Robots can not fight for both teams')

        return data


class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ['id', 'r1', 'r2', 'winner']

    def validate(self, data):
        if data['r1'] == data['r2']:
            raise ValidationError('A robot cannot battle itself')

        if data['winner'] is None:
            raise ValidationError('No winner selected')

        if data['winner'] not in (data['r1'], data['r2']):
            raise ValidationError('Only battle participants can win.' +
                                  ' Expected %s or %s, got %s' %
                                  (data['r1'], data['r2'], data['winner']))

        return data
