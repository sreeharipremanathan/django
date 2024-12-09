from rest_framework import serializers
from .models import *

class Sample(serializers.Serializer):
    roll_no=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()

class model_serializers(serializers.Serializer):
    class meta:
        model=Student
        feilds='__all__'