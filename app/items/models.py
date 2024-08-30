from django.db import models


class Item(models.Model):
    stripe_item_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, default='usd')


    def __str__(self):
        return self.name
    
class Discount(models.Model):
    code = models.CharField(max_length=255, unique=True)
    percent_discount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.percent_discount}%"


class Tax(models.Model):
    name = models.CharField(max_length=255)
    count_tax = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.count_tax}%"

class Order(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Item, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discounts = models.ManyToManyField(Discount, blank=True)
    taxes = models.ManyToManyField(Tax, blank=True)

    def __str__(self):
        if self.id:
            return f"Ordef #{self.id} - {self.total_price}"
        return f"Order (unsaved) - {self.total_price}"
        
    
    def calculate_total_price(self):
        total = sum(order_item.item.price * order_item.count for order_item in self.orderitem_set.all())
        for discount in self.discounts.all():
            total -= total * (discount.percent_discount / 100)
        for tax in self.taxes.all():
            total += total * (tax.count_tax / 100)
        self.total_price = total
        super().save()
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.count} * {self.item.name} for Order #{self.order.id}"
    

