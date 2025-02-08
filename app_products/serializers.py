from rest_framework import serializers

from app_products.models import ProductsModel


class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'