from collections import OrderedDict

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

IZI_SHOP_NAME = 'IZI'
IZI_SHOP_TAGLINE = ''
IZI_HOMEPAGE = reverse_lazy('promotions:home')

# Dynamic class loading
IZI_DYNAMIC_CLASS_LOADER = 'izi.core.loading.default_class_loader'

# Basket settings
IZI_BASKET_COOKIE_LIFETIME = 7 * 24 * 60 * 60
IZI_BASKET_COOKIE_OPEN = 'izi_open_basket'
IZI_BASKET_COOKIE_SECURE = False
IZI_MAX_BASKET_QUANTITY_THRESHOLD = 10000

# Recently-viewed products
IZI_RECENTLY_VIEWED_COOKIE_LIFETIME = 7 * 24 * 60 * 60
IZI_RECENTLY_VIEWED_COOKIE_NAME = 'izi_history'
IZI_RECENTLY_VIEWED_COOKIE_SECURE = False
IZI_RECENTLY_VIEWED_PRODUCTS = 20

# Currency
IZI_DEFAULT_CURRENCY = 'GBP'

# Paths
IZI_IMAGE_FOLDER = 'images/products/%Y/%m/'
IZI_PROMOTION_FOLDER = 'images/promotions/'
IZI_DELETE_IMAGE_FILES = True

# Copy this image from izi/static/img to your MEDIA_ROOT folder.
# It needs to be there so Sorl can resize it.
IZI_MISSING_IMAGE_URL = 'image_not_found.jpg'
IZI_UPLOAD_ROOT = '/tmp'

# Address settings
IZI_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4', 'postcode', 'country')

# Pagination settings

IZI_OFFERS_PER_PAGE = 20
IZI_PRODUCTS_PER_PAGE = 20
IZI_REVIEWS_PER_PAGE = 20
IZI_NOTIFICATIONS_PER_PAGE = 20
IZI_EMAILS_PER_PAGE = 20
IZI_ORDERS_PER_PAGE = 20
IZI_ADDRESSES_PER_PAGE = 20
IZI_STOCK_ALERTS_PER_PAGE = 20
IZI_DASHBOARD_ITEMS_PER_PAGE = 20

# Checkout
IZI_ALLOW_ANON_CHECKOUT = False

# Promotions
IZI_PROMOTION_POSITIONS = (('page', 'Page'),
                             ('right', 'Right-hand sidebar'),
                             ('left', 'Left-hand sidebar'))

# Reviews
IZI_ALLOW_ANON_REVIEWS = True
IZI_MODERATE_REVIEWS = False

# Accounts
IZI_ACCOUNTS_REDIRECT_URL = 'customer:profile-view'

# This enables sending alert notifications/emails instantly when products get
# back in stock by listening to stock record update signals.
# This might impact performance for large numbers of stock record updates.
# Alternatively, the management command ``izi_send_alerts`` can be used to
# run periodically, e.g. as a cron job. In this case eager alerts should be
# disabled.
IZI_EAGER_ALERTS = True

# Registration
IZI_SEND_REGISTRATION_EMAIL = True
IZI_FROM_EMAIL = 'izi@example.com'

# Slug handling
IZI_SLUG_FUNCTION = 'izi.core.utils.default_slugifier'
IZI_SLUG_MAP = {}
IZI_SLUG_BLACKLIST = []
IZI_SLUG_ALLOW_UNICODE = False

# Cookies
IZI_COOKIES_DELETE_ON_LOGOUT = ['izi_recently_viewed_products', ]

# Hidden IZI features, e.g. wishlists or reviews
IZI_HIDDEN_FEATURES = []

# Menu structure of the dashboard navigation
IZI_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
            {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
            },
            {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
            },
        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': _('Orders'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
            },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'children': [
            {
                'label': _('Customers'),
                'url_name': 'dashboard:users-index',
            },
            {
                'label': _('Stock alert requests'),
                'url_name': 'dashboard:user-alert-list',
            },
        ]
    },
    {
        'label': _('Offers'),
        'icon': 'icon-bullhorn',
        'children': [
            {
                'label': _('Offers'),
                'url_name': 'dashboard:offer-list',
            },
            {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
            {
                'label': _('Voucher Sets'),
                'url_name': 'dashboard:voucher-set-list',
            },

        ],
    },
    {
        'label': _('Content'),
        'icon': 'icon-folder-close',
        'children': [
            {
                'label': _('Content blocks'),
                'url_name': 'dashboard:promotion-list',
            },
            {
                'label': _('Content blocks by page'),
                'url_name': 'dashboard:promotion-list-by-page',
            },
            {
                'label': _('Pages'),
                'url_name': 'dashboard:page-list',
            },
            {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
            },
            {
                'label': _('Reviews'),
                'url_name': 'dashboard:reviews-list',
            },
        ]
    },
    {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
    },
]
IZI_DASHBOARD_DEFAULT_ACCESS_FUNCTION = 'izi.apps.dashboard.nav.default_access_fn'  # noqa

# Search facets
IZI_SEARCH_FACETS = {
    'fields': OrderedDict([
        # The key for these dicts will be used when passing facet data
        # to the template. Same for the 'queries' dict below.
        ('product_class', {'name': _('Type'), 'field': 'product_class'}),
        ('rating', {'name': _('Rating'), 'field': 'rating'}),
        # You can specify an 'options' element that will be passed to the
        # SearchQuerySet.facet() call.
        # For instance, with Elasticsearch backend, 'options': {'order': 'term'}
        # will sort items in a facet by title instead of number of items.
        # It's hard to get 'missing' to work
        # correctly though as of Solr's hilarious syntax for selecting
        # items without a specific facet:
        # http://wiki.apache.org/solr/SimpleFacetParameters#facet.method
        # 'options': {'missing': 'true'}
    ]),
    'queries': OrderedDict([
        ('price_range',
         {
             'name': _('Price range'),
             'field': 'price',
             'queries': [
                 # This is a list of (name, query) tuples where the name will
                 # be displayed on the front-end.
                 (_('0 to 20'), '[0 TO 20]'),
                 (_('20 to 40'), '[20 TO 40]'),
                 (_('40 to 60'), '[40 TO 60]'),
                 (_('60+'), '[60 TO *]'),
             ]
         }),
    ]),
}


IZI_PROMOTIONS_ENABLED = True
IZI_PRODUCT_SEARCH_HANDLER = None
