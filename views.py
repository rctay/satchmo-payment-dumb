from django.views.decorators.cache import never_cache
from livesettings import config_get_group
from payment.views import payship
from payment.views.confirm import ConfirmController

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
