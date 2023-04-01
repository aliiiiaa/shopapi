from rest_framework import serializers
from product.models import Product, Review, Category, Tags
from rest_framework.exceptions import ValidationError


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
        fields = 'name products_count'.split()


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating'.split()


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = 'name'


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    descriptions = serializers.CharField(required=False, default='no descriptions')
    price = serializers.IntegerField(default=0)
    category_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField())

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError(f'Category with id [{category_id}] not found')
        return category_id


    def validate_tags(self, tags):
        try:
            tag_ids = list(Tags.objects.filter(id__in=tags).values_list('id', flat=True))
            invalid_ids = set(tags) - set(tag_ids)
        except Tags.DoesNotExist:
                raise ValidationError(f'product with id ({", ".join(str(id) for id in invalid_ids)}) not found!')
        return tag_ids

