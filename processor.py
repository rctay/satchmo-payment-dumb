from decimal import Decimal

from django.utils.translation import ugettext_lazy as _
from livesettings import config_value, config_get_group
from payment.modules.base import HeadlessPaymentProcessor, ProcessorResult

config = config_get_group('PAYMENT_DUMB')

class PaymentProcessor(HeadlessPaymentProcessor):
    def __init__(self, settings):
        super(PaymentProcessor, self).__init__('dumb', settings)

    def capture_payment(self, testing=False, order=None, amount=Decimal('0')):
        """
        Users are expected to implement recording of payments, so we just return
        a blanket success.
        """
        if not config_value(config, 'LIVE'):
            payment = self.record_payment(order=order, amount=amount,
                transaction_id="TESTING", reason_code='0')

        return ProcessorResult(self.key, True, _('Skipping payment recording'))
