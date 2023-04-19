from django.db import models

# Product model
class Product(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lowest_price = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.name}"

# Variations model
class Variations(models.Model):
    ID = models.AutoField(primary_key=True)
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_text = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.product_ID.name}: {self.variation_text}"