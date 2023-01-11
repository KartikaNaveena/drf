from rest_framework import serializers
from .models import Person,Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
    def validate(self,data):
        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        return data