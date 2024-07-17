from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Offer(models.Model):
    product = models.ForeignKey(Product, related_name='offers', on_delete=models.CASCADE)
    discount = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.discount}% off on {self.product.name}"

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    saved_for_later = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
