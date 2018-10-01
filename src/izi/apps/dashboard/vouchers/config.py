from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VouchersDashboardConfig(AppConfig):
    label = 'vouchers_dashboard'
    name = 'izi.apps.dashboard.vouchers'
    verbose_name = _('Vouchers dashboard')
