from django.http import HttpResponseRedirect
from satchmo_store.shop.models import Order, OrderStatus

from signals import pending_order_confirmed

def _dumb_success(controller):
    """
    Stripped-down implementation of `ConfirmController._onSuccess()`:

      - removed check for whether order has been paid in full
      - remove code for subscription products
      - changed order status
    """
    controller.cart.empty()
    try:
        curr_status = controller.order.orderstatus_set.latest()
    except OrderStatus.DoesNotExist:
        curr_status = None

    if (curr_status is None) or (curr_status.notes and curr_status.status == "New"):
        controller.order.add_status(status='New', notes = "Order pending payment")
    else:
        # otherwise just update and save
        if not curr_status.notes:
            curr_status.notes = _("Order pending payment")
        curr_status.save()

    # notify listeners
    pending_order_confirmed.send(controller, order=controller.order)

    #Redirect to the success page
    url = controller.lookup_url('satchmo_checkout-success')
    return HttpResponseRedirect(url)
