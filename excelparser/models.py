from django.db import models

class Product(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    lowest_price = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add = True, editable=False)

    def __str__(self):
        return f"{self.name}"

class Variations(models.Model):
    ID = models.IntegerField(primary_key=True)
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_text = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add = True, editable=False)

    def __str__(self):
        return f"{self.product_ID.name}: {self.variation_text}"