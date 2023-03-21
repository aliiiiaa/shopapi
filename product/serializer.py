from rest_framework import serializers
from product.models import Product, Review, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title price category'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'
