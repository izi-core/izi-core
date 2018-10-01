==============
IZI settings
==============

This is a comprehensive list of all the settings IZI provides.  All settings
are optional.

Display settings
================

``IZI_SHOP_NAME``
-------------------

Default: ``'IZI'``

The name of your e-commerce shop site.  This is shown as the main logo within
the default templates.

``IZI_SHOP_TAGLINE``
----------------------

Default: ``''``

The tagline that is displayed next to the shop name and in the browser title.

``IZI_HOMEPAGE``
------------------

Default: ``reverse_lazy('promotions:home')``

URL of home page of your site. This value is used for `Home` link in
navigation and redirection page after logout. Useful if you use a different app
to serve your homepage.

``IZI_ACCOUNTS_REDIRECT_URL``
-------------------------------

Default: ``'customer:profile-view'``

IZI has a view that gets called any time the user clicks on 'My account' or
similar. By default it's a dumb redirect to the view configured with this
setting. But you could also override the view to display a more useful
account summary page or such like.

``IZI_RECENTLY_VIEWED_PRODUCTS``
----------------------------------

Default: 20

The number of recently viewed products to store.

``IZI_RECENTLY_VIEWED_COOKIE_LIFETIME``
-----------------------------------------

Default: 604800 (1 week in seconds)

The time to live for the cookie in seconds.

``IZI_RECENTLY_VIEWED_COOKIE_NAME``
-------------------------------------

Default: ``'izi_history'``

The name of the cookie for showing recently viewed products.

``IZI_HIDDEN_FEATURES``
-------------------------

Defaults: ``[]``

Allows to disable particular IZI feature in application and templates.
More information in the :doc:`/howto/how_to_disable_an_app_or_feature` document.

Pagination
----------

There are a number of settings that control pagination in IZI's views. They
all default to 20.

- ``IZI_PRODUCTS_PER_PAGE``
- ``IZI_OFFERS_PER_PAGE``
- ``IZI_REVIEWS_PER_PAGE``
- ``IZI_NOTIFICATIONS_PER_PAGE``
- ``IZI_EMAILS_PER_PAGE``
- ``IZI_ORDERS_PER_PAGE``
- ``IZI_ADDRESSES_PER_PAGE``
- ``IZI_STOCK_ALERTS_PER_PAGE``
- ``IZI_DASHBOARD_ITEMS_PER_PAGE``

.. _izi_search_facets:

``IZI_SEARCH_FACETS``
-----------------------

A dictionary that specifies the facets to use with the search backend.  It
needs to be a dict with keys ``fields`` and ``queries`` for field- and
query-type facets. Field-type facets can get an 'options' element with parameters like facet
sorting, filtering, etc.
The default is::

    IZI_SEARCH_FACETS = {
        'fields': OrderedDict([
            ('product_class', {'name': _('Type'), 'field': 'product_class'}),
            ('rating', {'name': _('Rating'), 'field': 'rating'}),
        ]),
        'queries': OrderedDict([
            ('price_range',
             {
                 'name': _('Price range'),
                 'field': 'price',
                 'queries': [
                     # This is a list of (name, query) tuples where the name will
                     # be displayed on the front-end.
                     (_('0 to 20'), u'[0 TO 20]'),
                     (_('20 to 40'), u'[20 TO 40]'),
                     (_('40 to 60'), u'[40 TO 60]'),
                     (_('60+'), u'[60 TO *]'),
                 ]
             }),
        ]),
    }

``IZI_PRODUCT_SEARCH_HANDLER``
--------------------------------

The search handler to be used in the product list views. If ``None``,
IZI tries to guess the correct handler based on your Haystack settings.

Default::

    None

``IZI_PROMOTION_POSITIONS``
-----------------------------

Default::

    IZI_PROMOTION_POSITIONS = (('page', 'Page'),
                                 ('right', 'Right-hand sidebar'),
                                 ('left', 'Left-hand sidebar'))

The choice of display locations available when editing a promotion. Only
useful when using a new set of templates.

.. _IZI_DASHBOARD_NAVIGATION:

``IZI_DASHBOARD_NAVIGATION``
------------------------------

Default: see ``izi.defaults`` (too long to include here).

A list of dashboard navigation elements. Usage is explained in
:doc:`/howto/how_to_configure_the_dashboard_navigation`.

``IZI_DASHBOARD_DEFAULT_ACCESS_FUNCTION``
-------------------------------------------

Default: ``'izi.apps.dashboard.nav.default_access_fn'``

``IZI_DASHBOARD_NAVIGATION`` allows passing an access function for each node
which is used to determine whether to show the node for a specific user or not.
If no access function is defined, the function specified here is used.
The default function integrates with the permission-based dashboard and shows
the node if the user will be able to access it. That should be sufficient for
most cases.

Order settings
==============

``IZI_INITIAL_ORDER_STATUS``
------------------------------

The initial status used when a new order is submitted. This has to be a status
that is defined in the ``IZI_ORDER_STATUS_PIPELINE``.

``IZI_INITIAL_LINE_STATUS``
-----------------------------

The status assigned to a line item when it is created as part of an new order. It
has to be a status defined in ``IZI_LINE_STATUS_PIPELINE``.

``IZI_ORDER_STATUS_PIPELINE``
-------------------------------

Default: ``{}``

The pipeline defines the statuses that an order or line item can have and what
transitions are allowed in any given status. The pipeline is defined as a
dictionary where the keys are the available statuses. Allowed transitions are
defined as iterable values for the corresponding status.

A sample pipeline (as used in the IZI sandbox) might look like this::

    IZI_INITIAL_ORDER_STATUS = 'Pending'
    IZI_INITIAL_LINE_STATUS = 'Pending'
    IZI_ORDER_STATUS_PIPELINE = {
        'Pending': ('Being processed', 'Cancelled',),
        'Being processed': ('Processed', 'Cancelled',),
        'Cancelled': (),
    }

``IZI_ORDER_STATUS_CASCADE``
------------------------------

This defines a mapping of status changes for order lines which 'cascade' down
from an order status change.

For example::

    IZI_ORDER_STATUS_CASCADE = {
        'Being processed': 'In progress'
    }

With this mapping, when an order has it's status set to 'Being processed', all
lines within it have their status set to 'In progress'.  In a sense, the status
change cascades down to the related objects.

Note that this cascade ignores restrictions from the
``IZI_LINE_STATUS_PIPELINE``.

``IZI_LINE_STATUS_PIPELINE``
------------------------------

Default: ``{}``

Same as ``IZI_ORDER_STATUS_PIPELINE`` but for lines.

Checkout settings
=================

``IZI_ALLOW_ANON_CHECKOUT``
-----------------------------

Default: ``False``

Specifies if an anonymous user can buy products without creating an account
first.  If set to ``False`` users are required to authenticate before they can
checkout (using IZI's default checkout views).

``IZI_REQUIRED_ADDRESS_FIELDS``
---------------------------------

Default: ``('first_name', 'last_name', 'line1', 'line4', 'postcode', 'country')``

List of form fields that a user has to fill out to validate an address field.

Review settings
===============

``IZI_ALLOW_ANON_REVIEWS``
----------------------------

Default: ``True``

This setting defines whether an anonymous user can create a review for
a product without registering first. If it is set to ``True`` anonymous
users can create product reviews.

``IZI_MODERATE_REVIEWS``
--------------------------

Default: ``False``

This defines whether reviews have to be moderated before they are publicly
available. If set to ``False`` a review created by a customer is immediately
visible on the product page.

Communication settings
======================

``IZI_EAGER_ALERTS``
----------------------

Default: ``True``

This enables sending alert notifications/emails instantly when products get
back in stock by listening to stock record update signals this might impact
performance for large numbers stock record updates.
Alternatively, the management command ``izi_send_alerts`` can be used to
run periodically, e.g. as a cronjob. In this case instant alerts should be
disabled.

``IZI_SEND_REGISTRATION_EMAIL``
---------------------------------

Default: ``True``

Sending out *welcome* messages to a user after they have registered on the
site can be enabled or disabled using this setting. Setting it to ``True``
will send out emails on registration.

``IZI_FROM_EMAIL``
--------------------

Default: ``izi@example.com``

The email address used as the sender for all communication events and emails
handled by IZI.

``IZI_STATIC_BASE_URL``
-------------------------

Default: ``None``

A URL which is passed into the templates for communication events.  It is not
used in IZI's default templates but could be used to include static assets
(eg images) in a HTML email template.

Offer settings
==============

``IZI_OFFER_ROUNDING_FUNCTION``
---------------------------------

Default: Round down to the nearest hundredth of a unit using ``decimal.Decimal.quantize``

A function responsible for rounding decimal amounts when offer discount
calculations don't lead to legitimate currency values.

Basket settings
===============

``IZI_BASKET_COOKIE_LIFETIME``
--------------------------------

Default: 604800 (1 week in seconds)

The time to live for the basket cookie in seconds.

``IZI_MAX_BASKET_QUANTITY_THRESHOLD``
---------------------------------------

Default: ``10000``

The maximum number of products that can be added to a basket at once. Set to 
``None`` to disable the basket treshold limitation.


``IZI_BASKET_COOKIE_OPEN``
----------------------------

Default: ``'izi_open_basket'``

The name of the cookie for the open basket.

Currency settings
=================

``IZI_DEFAULT_CURRENCY``
--------------------------

Default: ``GBP``

This should be the symbol of the currency you wish IZI to use by default.
This will be used by the currency templatetag.

.. _currency-format-setting:

``IZI_CURRENCY_FORMAT``
-------------------------

Default: ``None``

Dictionary with arguments for the ``format_currency`` function from the `Babel library`_.
Contains next options: `format`, `format_type`, `currency_digits`.
For example::

    IZI_CURRENCY_FORMAT = {
        'USD': {
            'currency_digits': False,
            'format_type': "accounting",
        },
        'EUR': {
            'format': u'#,##0\xa0¤',
        }
    }

.. _`Babel library`: http://babel.pocoo.org/en/latest/api/numbers.html#babel.numbers.format_currency

Upload/media settings
=====================

``IZI_IMAGE_FOLDER``
----------------------

Default: ``images/products/%Y/%m/``

The location within the ``MEDIA_ROOT`` folder that is used to store product images.
The folder name can contain date format strings as described in the `Django Docs`_.

.. _`Django Docs`: https://docs.djangoproject.com/en/stable/ref/models/fields/#filefield

``IZI_DELETE_IMAGE_FILES``
----------------------------

Default: ``True``

If enabled, a ``post_delete`` hook will attempt to delete any image files and
created thumbnails when a model with an ``ImageField`` is deleted. This is
usually desired, but might not be what you want when using a remote storage.


``IZI_PROMOTION_FOLDER``
--------------------------

Default: ``images/promotions/``

The folder within ``MEDIA_ROOT`` used for uploaded promotion images.

.. _missing-image-label:

``IZI_MISSING_IMAGE_URL``
---------------------------

Default: ``image_not_found.jpg``

Copy this image from ``izi/static/img`` to your ``MEDIA_ROOT`` folder. It needs to
be there so Sorl can resize it.

``IZI_UPLOAD_ROOT``
---------------------

Default: ``/tmp``

The folder is used to temporarily hold uploaded files until they are processed.
Such files should always be deleted afterwards.

Slug settings
=============

``IZI_SLUG_FUNCTION``
-----------------------

Default: ``'izi.core.utils.default_slugifier'``

A dotted path to the slugify function to use.

Example::

    # in myproject.utils
    def some_slugify(value, allow_unicode=False):
        return value

    # in settings.py
    IZI_SLUG_FUNCTION = 'myproject.utils.some_slugify'

``IZI_SLUG_MAP``
------------------

Default: ``{}``

A dictionary to target:replacement strings that the slugify will apply before
slugifying the value. This is useful when names contain characters which would
normally be stripped. For instance::

    IZI_SLUG_MAP = {
        'c++': 'cpp',
        'f#': 'fsharp',
    }

``IZI_SLUG_BLACKLIST``
------------------------

Default: ``[]``

An iterable of words the slugify will try to remove after the value has been
slugified. Note, a word will not be removed from the slug if it would
result in an empty slug.

Example::

    # With IZI_SLUG_BLACKLIST = ['the']
    slugify('The cat')
    > 'cat'

    # With IZI_SLUG_BLACKLIST = ['the', 'cat']
    slugify('The cat')
    > 'cat'

``IZI_SLUG_ALLOW_UNICODE``
----------------------------

Default: ``False``

Allows unicode characters in slugs generated by ``AutoSlugField``,
which is supported by the underlying ``SlugField`` in Django>=1.9.


Dynamic importer settings
=========================

``IZI_DYNAMIC_CLASS_LOADER``
----------------------------------

Default: ``izi.core.loading.default_class_loader``

A dotted path to the callable used to dynamically import classes.


Misc settings
=============

``IZI_COOKIES_DELETE_ON_LOGOUT``
----------------------------------

Default: ``['izi_recently_viewed_products',]``

Which cookies to delete automatically when the user logs out.

``IZI_GOOGLE_ANALYTICS_ID``
-----------------------------

Tracking ID for Google Analytics tracking code, available as `google_analytics_id` in the template
context. If setting is set, enables Universal Analytics tracking code for page views and
transactions.


``IZI_USE_LESS``
------------------

Allows to use raw LESS styles directly. Refer to :ref:`less-css` document for more details.


``IZI_CSV_INCLUDE_BOM``
-------------------------

Default: ``False``

A flag to control whether IZI's CSV writer should prepend a byte order mark
(BOM) to CSV files that are encoded in UTF-8. Useful for compatibility with some
CSV readers, Microsoft Excel in particular.
