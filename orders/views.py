from django.shortcuts import render, redirect
from.models import Order,OrderedItem
from products.models import Product
from customers.models import Customer

def show_cart(request):
    print("hi")
    customer = Customer.objects.get(user_id=request.user.id)
    print(f"User C - {customer.phone}")
    cart_obj=Order.objects.get(
        ower=customer,
        order_status=Order.CART_STAGE
    )
    print(f"Order C - {cart_obj.id}")
    context={'cart' :cart_obj}
    return render(request, 'cart.html',context=context)

def add_to_cart(request):
    if request.POST:

        customer = Customer.objects.get(user_id=request.user.id)
        quantity=request.POST.get('quantity')
        product_id=request.POST.get('product_id')
        print(f"User - {request.user.id}")
        print(f"User C - {customer.phone}")
        print(f"Qty - {quantity}")
        print(f"Pdt - {product_id}")
        cart_obj,created=Order.objects.get_or_create(
            ower=customer,
            order_status=Order.CART_STAGE
        )
        print(created)
        product=Product.objects.get(pk=product_id)
        ordered_item=OrderedItem.objects.create(
            Product= product,
            ower=cart_obj,
            quantity=quantity
        )
        return redirect('cart')