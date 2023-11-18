from rest_framework import serializers
from .models import Product, Variety, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class VarietySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Variety
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    variety = VarietySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'category', 'feature', 'variety']

