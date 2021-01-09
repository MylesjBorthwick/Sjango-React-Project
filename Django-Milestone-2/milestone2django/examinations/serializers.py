from rest_framework import serializers
from .models import Examinations


class Examinations_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Examinations
    fields = ('examination_id', 'publicID', 'name')

