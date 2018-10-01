from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PartnerConfig(AppConfig):
    label = 'partner'
    name = 'izi.apps.partner'
    verbose_name = _('Partner')

    def ready(self):
        from . import receivers  # noqa
