from livesettings import *
from django.utils.translation import ugettext_lazy as _

PAYMENT_GROUP = ConfigurationGroup('PAYMENT_DUMB',
    _('Dumb Payment Module Settings'),
    ordering = 200)

config_register_list(
    ModuleValue(PAYMENT_GROUP,
        'MODULE',
        description=_('Implementation module'),
        hidden=True,
        default = 'satchmo_payment_dumb'),

    BooleanValue(PAYMENT_GROUP,
        'LIVE',
        description=_("Accept real payments"),
        help_text=_("False if you want to be in test mode"),
        default=False),

    BooleanValue(PAYMENT_GROUP,
        'SSL',
        description=_("Use SSL for the module checkout pages?"),
        default=False),

    StringValue(PAYMENT_GROUP,
        'KEY',
        description=_("Module key"),
        hidden=True,
        default = 'DUMB'),

    StringValue(PAYMENT_GROUP,
        'LABEL',
        description=_('English name for this group on the checkout screens'),
        default = 'Pay Now',
        help_text = _('This will be passed to the translation utility')),

    # We can't use the `^<base>/` form like the built-in satchmo payment modules
    # do, as we're prefixing it with `^/checkout/%s/`.
    StringValue(PAYMENT_GROUP,
        'URL_BASE',
        description=_('The url base used for constructing urlpatterns which will use this module'),
        help_text = _('Please do not add the \'^\' or trailing \'/\'; this is done for you.'),
        default = 'dumb'),
)
