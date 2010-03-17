from django.conf.urls.defaults import url, include
from livesettings import config_get_group, config_value
from satchmo_store import shop
from signals_ahoy.signals import collect_urls

config_group = config_get_group('PAYMENT_DUMB')

def add_dumb_urls(sender, patterns=None, **kwargs):
    patterns.append(
        url(r'^checkout/%s/' % config_value(config_group, 'URL_BASE'),
            include('%s.urls' % config_value(config_group, 'MODULE').__name__),)
    )

collect_urls.connect(add_dumb_urls, sender=shop)
