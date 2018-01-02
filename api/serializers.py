from rest_framework import serializers
from api import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Item
        fields='id','topic','description'

class marksSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.marks
        fields='id','rollno','marks'



