from django.urls import path
from .views import buy_item, item_detail, index

urlpatterns = [
    path('', index, name='index'),
    path('buy/<int:id>', buy_item, name='buy_item'),
    path('item/<int:id>', item_detail, name='item_detail'),
]