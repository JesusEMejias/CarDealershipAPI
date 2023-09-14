from rest_framework import serializers

from CarDealershipAPI import models


class carProfileSerializer (serializers.ModelSerializer):
    """Serializer for de Car Profile Model"""
    
    class Meta:
        model = models.carProfile
        fields = ('id', 'carBrand', 'carModel')
    
    def create (self, validated_data):
        carProfile = models.carProfile.objects.createCar(
            carBrand = validated_data['carBrand'],
            carModel = validated_data['carModel'],
        )
        
        return carProfile