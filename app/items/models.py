from django.db import models


class Item(models.Model):
    stripe_item_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    