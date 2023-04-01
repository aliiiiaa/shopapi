from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializer import ProductSerializer, ReviewSerializer, CategorySerializer, RatingSerializer, TagsSerializer
from product.models import Product, Review, Category,Tags
from rest_framework import status


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        tags = request.data.get('tags')
        product = Product.objects.create(title=title, description=description, price=price,
                                         category_id=category_id)
        product.tags.set(tags)
        product.save()
        return Response(data=ProductSerializer(product).data)


@api_view(['PUT', 'DELETE', 'GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.tags = request.data.get('tags')
        product.save()
        return Response(data=ProductSerializer(product).data)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        star = request.data.get('star')
        product_id = request.data.get('product_id')
        review = Review.objects.create(text=text, star=star, product_id=product_id)
        review.save()
        return Response(data=ReviewSerializer(review).data)


@api_view(['PUT', 'DELETE', 'GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.star = request.data.get('star')
        review.product_id = request.data.get('product_id')
        review.save()
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(name=name)
        category.save()
        return Response(data=CategorySerializer(category).data)


@api_view(['PUT', 'DELETE', 'GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except category.DoesNotExist:
        return Response(data={'error': 'category not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(data=CategorySerializer(category).data)


@api_view(['GET', 'POST'])
def tags_list_api_view(request):
    if request.method == 'GET':
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        tags = Tags.objects.create(name=name)
        tags.save()
        return Response(data=TagsSerializer(tags).data)


@api_view(['GET', 'PUT', 'DELETE'])
def tags_detail_api_view(request, id):
    try:
        tags = Tags.objects.get(id=id)
    except tags.DoesNotExist:
        return Response(data={'error': 'tags not found!'},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def products_reviews_view(request):
    product = Product.objects.all()
    serializer = RatingSerializer(product, many=True)
    return Response(data=serializer.data)