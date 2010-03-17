from django.conf.urls.defaults import url, include
from django.utils.translation import ugettext_lazy as _
from livesettings import config_get_group, config_value
from payment.signals import payment_choices
from satchmo_store import shop
from signals_ahoy.signals import collect_urls

config_group = config_get_group('PAYMENT_DUMB')

def add_dumb_urls(sender, patterns=None, **kwargs):
    patterns.append(
        url(r'^checkout/%s/' % config_value(config_group, 'URL_BASE'),
            include('%s.urls' % config_value(config_group, 'MODULE').__name__),)
    )

collect_urls.connect(add_dumb_urls, sender=shop)

def add_dumb_method(sender, choices=None, **kwargs):
    """
    The `payment_choices` signal doesn't really allow us cover all the bases -
    `payment.active_gateways()` is the one to hack.

    But it's close.
    """
    if not choices:
        return

    module = config_value(config_group, 'MODULE')
    group = 'PAYMENT_DUMB'

    # repeat logic in `payment.config.labelled_gateway_choices()`
    defaultlabel = module.__name__.split('.')[-1]
    label = _(config_value(group, 'LABEL', default = defaultlabel))
    choices.append((group, label))

payment_choices.connect(add_dumb_method)
