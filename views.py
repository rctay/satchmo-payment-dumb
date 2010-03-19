from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from livesettings import config_get_group
from payment.views import payship
from payment.views.confirm import ConfirmController
from satchmo_store.shop.models import Order
from satchmo_utils.views import bad_or_missing

from utils import _dumb_success

config_group = config_get_group('PAYMENT_DUMB')

def pay_ship_info(request, template='shop/checkout/dumb/pay_ship.html'):
    return payship.base_pay_ship_info(request, config_group,
        payship.simple_pay_ship_process_form, template)
pay_ship_info = never_cache(pay_ship_info)

def confirm_info(request, template='shop/checkout/dumb/confirm.html'):
    """
    We need to override the `onSuccess` property of the Controller, so we're
    re-implementing `confirm.credit_confirm_info()` - it's only a few lines anyway.
    """
    controller = ConfirmController(request, config_group)
    controller.templates['CONFIRM'] = template
    # the magic I need.
    controller.onSuccess = _dumb_success
    controller.confirm()
    return controller.response

    return confirm.credit_confirm_info(request, config_group, template)
confirm_info = never_cache(confirm_info)

def success(request, template='shop/checkout/dumb/success.html'):
    """
    We re-implement `payment.views.checkout.success()`, as it doesn't allow one
    to change the template (to `shop/checkout/dumb/success.html`).

    Overriding this template takes out all the guesswork: you *know* that it is
    this 'dumb' module that landed the user there.

    Changes from default implementation:

     * rework error message to account for no-order case
    """
    try:
        order = Order.objects.from_request(request)
    except Order.DoesNotExist:
        return bad_or_missing(request, _('Either your order has already been processed, or you do not have an order in progress.'))

    del request.session['orderID']
    return render_to_response(template, {'order': order},
                              context_instance=RequestContext(request))
success = never_cache(success)
