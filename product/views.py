from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializer import ProductSerializer, ReviewSerializer, CategorySerializer, RatingSerializer
from product.models import Product, Review, Category
from rest_framework import status


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(data=serializer.data)


def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_list_api_view(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(data=serializer.data)


def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except category.DoesNotExist:
        return Response(data={'error': 'category not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def products_reviews_view(request):
    product = Product.objects.all()
    serializer = RatingSerializer(product, many=True)
    return Response(data=serializer.data)