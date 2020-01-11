from django.core.exceptions import ValidationError
from django.db import models


class Robot(models.Model):
    name = models.CharField(max_length=255)
    powermove = models.TextField()
    experience = models.IntegerField()
    out_of_order = models.BooleanField()
    avatar = models.URLField()

    def __str__(self):
        return '<Robot %s: %s>' % (self.id, self.name)


class Danceoff(models.Model):
    battles = models.ManyToManyField('Battle')

    def __str__(self):
        return '<Danceoff %s>' % (self.id)


class Battle(models.Model):

    r1 = models.ForeignKey(Robot, related_name='robot1',
                           on_delete=models.CASCADE,
                           limit_choices_to={'out_of_order': False})
    r2 = models.ForeignKey(Robot, related_name='robot2',
                           on_delete=models.CASCADE,
                           limit_choices_to={'out_of_order': False})
    winner = models.ForeignKey(
        Robot, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '<Battle %s: %s vs %s>' % (self.id, self.r1, self.r2)
