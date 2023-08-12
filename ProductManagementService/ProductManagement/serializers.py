from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FavProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
