from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShippingConfig(AppConfig):
    label = 'shipping'
    name = 'izi.apps.shipping'
    verbose_name = _('Shipping')
