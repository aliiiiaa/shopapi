from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def products_count(self):
        return self.product_set.count()


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        stars_list = [review.stars for review in self.reviews.all()]
        return sum(stars_list) // len(stars_list)


# STAR = ((iterator_, '*' * iterator_) for iterator_ in range(1, 6))


class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='review_list')
    star = models.IntegerField(default=5, choices=((iterator_, '*' * iterator_) for iterator_ in range(1, 6)))

    def __str__(self):
        return self.text



