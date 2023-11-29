from .models import Cart_tb,Cartitem
from .views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart_tb.objects.filter(cart_id=_cart_id(request))
            cart_items=Cartitem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart_tb.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)
