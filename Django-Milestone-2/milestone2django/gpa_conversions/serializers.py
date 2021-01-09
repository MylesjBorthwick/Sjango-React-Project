from rest_framework import serializers
from .models import GPA_Conversions


class GPA_Conversions_Serializer(serializers.ModelSerializer):
  class Meta:
    model = GPA_Conversions
    fields = ('id', 'lowerGrade', 'upperGrade', 'T_sign','name')

    