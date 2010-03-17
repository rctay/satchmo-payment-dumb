from django.views.decorators.cache import never_cache
from livesettings import config_get_group
from payment.views import confirm, payship

config_group = config_get_group('PAYMENT_DUMB')

def pay_ship_info(request, template='shop/checkout/dumb/pay_ship.html'):
    return payship.base_pay_ship_info(request, config_group,
        payship.simple_pay_ship_process_form, template)
pay_ship_info = never_cache(pay_ship_info)

def confirm_info(request, template='shop/checkout/dumb/confirm.html'):
    return confirm.credit_confirm_info(request, config_group, template)
confirm_info = never_cache(confirm_info)
