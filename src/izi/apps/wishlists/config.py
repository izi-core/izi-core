from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WishlistsConfig(AppConfig):
    label = 'wishlists'
    name = 'izi.apps.wishlists'
    verbose_name = _('Wishlists')
