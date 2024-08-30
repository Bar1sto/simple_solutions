from django.contrib import admin
from .models import Item, Order, OrderItem, Discount, Tax


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'create', 'update', 'total_price')
    readonly_fields = ['total_price']
    inlines = [OrderItemInline]
    filter_horizontal = ('discounts', 'taxes')

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'percent_discount')
    search_fields = ('code',)

class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_tax')
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'create', 'update', 'total_price')
    readonly_fields = ['total_price']
    inlines = [OrderItemInline]

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'percent_discount')
    search_fields = ('code',)

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_tax')
    search_fields = ('name',)

