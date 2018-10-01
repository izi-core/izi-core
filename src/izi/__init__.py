import os

# Use 'dev', 'beta', or 'final' as the 4th element to indicate release type.
VERSION = (2, 0, 0, 'dev')


def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    elif VERSION[3] != 'final':
        version = '%s %s' % (version, VERSION[3])
        if len(VERSION) == 5:
            version = '%s %s' % (version, VERSION[4])
    return version


# Cheeky setting that allows each template to be accessible by two paths.
# Eg: the template 'izi/templates/izi/base.html' can be accessed via both
# 'base.html' and 'izi/base.html'.  This allows IZI's templates to be
# extended by templates with the same filename
IZI_MAIN_TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates/izi')

IZI_CORE_APPS = [
    'izi',
    'izi.apps.analytics',
    'izi.apps.checkout',
    'izi.apps.address',
    'izi.apps.shipping',
    'izi.apps.catalogue',
    'izi.apps.catalogue.reviews',
    'izi.apps.partner',
    'izi.apps.basket',
    'izi.apps.payment',
    'izi.apps.offer',
    'izi.apps.order',
    'izi.apps.customer',
    'izi.apps.promotions',
    'izi.apps.search',
    'izi.apps.voucher',
    'izi.apps.wishlists',
    'izi.apps.dashboard',
    'izi.apps.dashboard.reports',
    'izi.apps.dashboard.users',
    'izi.apps.dashboard.orders',
    'izi.apps.dashboard.promotions',
    'izi.apps.dashboard.catalogue',
    'izi.apps.dashboard.offers',
    'izi.apps.dashboard.partners',
    'izi.apps.dashboard.pages',
    'izi.apps.dashboard.ranges',
    'izi.apps.dashboard.reviews',
    'izi.apps.dashboard.vouchers',
    'izi.apps.dashboard.communications',
    'izi.apps.dashboard.shipping',
    # 3rd-party apps that izi depends on
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'django_tables2',
]


def get_core_apps(overrides=None):
    """
    Return a list of izi's apps amended with any passed overrides
    """
    if not overrides:
        return IZI_CORE_APPS

    # Conservative import to ensure that this file can be loaded
    # without the presence Django.
    if isinstance(overrides, str):
        raise ValueError(
            "get_core_apps expects a list or tuple of apps "
            "to override")

    def get_app_label(app_label, overrides):
        pattern = app_label.replace('izi.apps.', '')
        for override in overrides:
            if override.endswith(pattern):
                if 'dashboard' in override and 'dashboard' not in pattern:
                    continue
                return override
        return app_label

    apps = []
    for app_label in IZI_CORE_APPS:
        apps.append(get_app_label(app_label, overrides))
    return apps
