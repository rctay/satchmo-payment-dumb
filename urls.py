from django.conf.urls.defaults import *
from livesettings import config_value, config_get_group

config = config_get_group('PAYMENT_DUMB')
module = config_value(config, 'MODULE').__name__
key = config_value(config, 'KEY')

urlpatterns = patterns('',
    (r'^$', '%s.views.pay_ship_info' % module,
        {'SSL':config.SSL.value}, '%s_satchmo_checkout-step2' % key),
    (r'^confirm/$', '%s.views.confirm_info' % module,
        {'SSL':config.SSL.value}, '%s_satchmo_checkout-step3' % key),
    (r'^success/$', 'payment.views.checkout.success',
        {'SSL':config.SSL.value}, '%s_satchmo_checkout-success' % key),
)
