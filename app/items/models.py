from django.db import models


class Item(models.Model):
    stripe_item_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    

class Order(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Ordef #{self.id} - {self.total_price}"
    
    def calculate_total_price(self):
        total = sum(Item.price for item in self.items.all())
        self.total_price = total
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.count} x {self.item.name} for Order #{self.order.id}"