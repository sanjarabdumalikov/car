from rest_framework import serializers
from .models import car,car_shop


class carserializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = '__all__'


class car_shopserilizer(serializers.ModelSerializer):
    class Meta:
        model = car_shop
        fields = '__all__'