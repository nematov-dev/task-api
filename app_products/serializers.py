from rest_framework import serializers

from app_products.models import PostsModel


class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = PostsModel
        fields = '__all__'