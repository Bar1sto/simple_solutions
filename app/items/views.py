import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import JsonResponse
from .models import Item, Order, OrderItem, Discount, Tax


stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, id):
    item = get_object_or_404(Item, id=id)

    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(item.price * 100),
            currency=item.currency,
            payment_method_types=['card'],
            description=f'Покупка: {item.name}'
        )
        return JsonResponse({'client_secret': payment_intent.client_secret})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


    # session = stripe.checkout.Session.create(
    #     payment_method_types=['card'],
    #     line_items=[{
    #         'price_data': {
    #             'currency': 'usd',
    #             'product_data': {
    #                 'name': item.name,
    #                 'description': item.description,
    #             },
    #             'unit_amount': int(item.price * 100),
    #         },
    #         'quantity': 1,
    #     }],
    #     mode='payment',
    #     success_url=request.build_absolute_uri('/success/'),
    #     cancel_url=request.build_absolute_uri('/cancel/'),
    # )
    # print('stripe_item_id:' + item.stripe_item_id, 'item name:' + item.name)
    # return JsonResponse({'session_id': session.id})

def create_check_session(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        order.calculate_total_price()
        url = request.build_absolute_uri('/')

        check_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': order_item.item.currency,
                        'product_data':
                        {
                            'name': order_item.item.name,
                        },
                        'unit_amount': int(order_item.item.price * 100),
                    },
                    'quantity': order_item.count,
                }
                for order_item in order.orderitem_set.all()
            ],
            mode='payment',
            discounts=[
                {
                    'coupon': discount.code,
                }
                for discount in order.discounts.all()
            ],
            tax_rates=[
                {
                    'display_name': tax.name,
                    'percent': tax.count_tax,
                }
                for tax in order.taxes.all()
            ],
            success_url=url + 'success/',
            cancel_url=url + 'cancel/',
        )

        return JsonResponse({'id': check_session.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def item_detail(request, id):
    item = get_object_or_404(Item, stripe_item_id=id)
    
    print(item.name)
    return render(request, 'items/items_detail.html', {
        'item': item,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    })

def index(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', {'items': items})