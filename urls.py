from django.conf.urls.defaults import *
from livesettings import config_value, config_get_group

config = config_get_group('PAYMENT_DUMB')

urlpatterns = patterns('',
    (r'^$', 'satchmo_payment_dumb.views.pay_ship_info',
        {'SSL':config.SSL.value}, 'DUMB_satchmo_checkout-step2'),
    (r'^confirm/$', 'satchmo_payment_dumb.views.confirm_info',
        {'SSL':config.SSL.value}, 'DUMB_satchmo_checkout-step3'),
    (r'^success/$', 'payment.views.checkout.success',
        {'SSL':config.SSL.value}, 'DUMB_satchmo_checkout-success'),
)
