from rest_framework import serializers
from TestApp.models import table1

class table1Serializer(serializers.ModelSerializer):
    class Meta:
        model = table1
        fields = (['tb1Id', 'tb1Name']) # fields that intended to be seen
