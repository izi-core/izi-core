.. image:: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/logos/izi.png
    :target: http://ecommerce.izi.asia

===================================
Domain-driven e-commerce for Django
===================================


IZI is an e-commerce framework for Django designed for building domain-driven
sites.  It is structured such that any part of the core functionality can be
customised to suit the needs of your project.  This allows a wide range of
e-commerce requirements to be handled, from large-scale B2C sites to complex B2B
sites rich in domain-specific business logic.

Contents:

.. contents:: :local:

.. image:: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/izicommerce.thumb.png
    :target: http://ecommerce.izi.asia

.. image:: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/readthedocs.thumb.png
    :target: https://izi-core.readthedocs.io/en/latest/

Further reading:

* `Official homepage`_
* `Sandbox site`_ (automatically deployed via the official docker sandbox image)
* `Documentation`_ on the excellent `readthedocs.org`_
* `Docker image`_ on http://hub.docker.com/
* `izi-core group`_ - mailing list for questions and announcements
* `izi-core-jobs group`_ - mailing list for job offers
* `Continuous integration homepage`_ on `travis-ci.org`_
* `Twitter account for news and updates`_
* #izi-core on Freenode (community-run IRC channel) with `public logs`_
* `Slack`_
* `PyPI page`_
* `Transifex project`_ - translating IZI made easy

.. start-no-pypi

Continuous integration status:

.. image:: https://travis-ci.org/izi-ecommerce/izi-core.svg?branch=master
    :target: https://travis-ci.org/izi-ecommerce/izi-core

.. image:: http://codecov.io/github/izi-core/izi-core/coverage.svg?branch=master
    :alt: Coverage
    :target: http://codecov.io/github/izi-core/izi-core?branch=master

.. image:: https://requires.io/github/izi-core/izi-core/requirements.svg?branch=master
     :target: https://requires.io/github/izi-core/izi-core/requirements/?branch=master
     :alt: Requirements Status

PyPI status:

.. image:: https://img.shields.io/pypi/v/izi-core.svg
    :target: https://pypi.python.org/pypi/izi-core/

Docs status:

.. image:: https://readthedocs.org/projects/izi-core/badge/
   :target: https://readthedocs.org/projects/izi-core/
   :alt: Documentation Status

.. end-no-pypi

.. _`Official homepage`: http://ecommerce.izi.asia
.. _`Sandbox site`: http://latest.ecommerce.izi.asia
.. _`Docker image`: https://hub.docker.com/r/izicommerce/izi-core-sandbox/
.. _`Documentation`: https://izi-core.readthedocs.io/en/latest/
.. _`readthedocs.org`: http://readthedocs.org
.. _`Continuous integration homepage`: http://travis-ci.org/#!/izi-core/izi-core
.. _`travis-ci.org`: http://travis-ci.org/
.. _`Twitter account for news and updates`: https://twitter.com/#!/django_izi
.. _`public logs`: https://botbot.me/freenode/izi-core/
.. _`izi-core group`: https://groups.google.com/forum/?fromgroups#!forum/izi-core
.. _`izi-core-jobs group`: https://groups.google.com/forum/?fromgroups#!forum/izi-core-jobs
.. _`PyPI page`: https://pypi.python.org/pypi/izi-core/
.. _`Transifex project`: https://www.transifex.com/projects/p/izi-core/
.. _`Slack`: https://slack.ecommerce.izi.asia/

Core team:

- `Daniel Do`_ (Twitter `@izi-global`_)

Screenshots
-----------

Sandbox
~~~~~~~

These are screenshots from the 'sandbox' example site that ships with
IZI.  It sports a simple design built with Twitter's Bootstrap_ and provides a
good starting point for rapidly building elegant e-commerce sites.

.. _Bootstrap: https://getbootstrap.com/

.. image:: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/browse.thumb.png
    :target: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/browse.png

.. image:: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/detail.thumb.png
    :target: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/detail.png

.. image:: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/basket.thumb.png
    :target: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/basket.png

.. image:: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/dashboard.thumb.png
    :target: https://github.com/izi-ecommerce/izi-core/raw/master/docs/images/screenshots/dashboard.png

The sandbox site is also available to browse at
https://latest.ecommerce.izi.asia.  Dashboard users can be created using `this
gateway page`_.

The sandbox site can be set-up locally `in 5 commands`_.  Want to
make changes?  Check out the `contributing guidelines`_.

.. _`this gateway page`: http://latest.ecommerce.izi.asia/gateway/
.. _`in 5 commands`: https://izi-core.readthedocs.io/en/latest/internals/sandbox.html#running-the-sandbox-locally
.. _`contributing guidelines`: https://izi-core.readthedocs.io/en/latest/internals/contributing/index.html


Extensions
----------

The following extensions are stable and ready for use:

* izi-core-api_ - RESTful JSON API for izi-core

* izi-core-adyen_ - Integration with the Adyen payment gateway

* izi-core-datacash_ - Integration with the DataCash_ payment gateway

* izi-core-paypal_ - Integration with PayPal.  This currently supports both
  `Express Checkout`_ and `PayFlow Pro`_.

* izi-core-paymentexpress_ - Integration with the `Payment Express`_ payment
  gateway

* izi-core-accounts_ - Managed accounts (can be used for giftcard
  functionality and loyalty schemes)

* izi-core-stores_ - Physical stores integration (opening hours, store
  locator etc)

* izi-core-eway_ - Integration with the eWay_ payment gateway.

* izi-core-sagepay-direct_ - Integration with "DIRECT" part of Sagepay's API

* django_izi_docdata_ - Integration with Docdata_ payment gateway.

* django_izi_invoices_ - Invoices or receipts generation for the
  IZI

.. _izi-core-api: https://github.com/izi-ecommerce/izi-core-api
.. _izi-core-adyen: https://github.com/izi-ecommerce/izi-core-adyen
.. _izi-core-datacash: https://github.com/izi-ecommerce/izi-core-datacash
.. _izi-core-paymentexpress: https://github.com/izi-ecommerce/izi-core-paymentexpress
.. _`Payment Express`: http://www.paymentexpress.com
.. _DataCash: http://www.datacash.com/
.. _izi-core-paypal: https://github.com/izi-ecommerce/izi-core-paypal
.. _`Express Checkout`: https://www.paypal.com/uk/cgi-bin/webscr?cmd=_additional-payment-ref-impl1
.. _`PayFlow Pro`: https://merchant.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=merchant/payment_gateway
.. _izi-core-accounts: https://github.com/izi-core/izi-accounts
.. _izi-core-easyrec: https://github.com/izi-ecommerce/izi-core-easyrec
.. _EasyRec: http://easyrec.org/
.. _izi-core-eway: https://github.com/snowball-one/izi-core-eway
.. _izi-core-stores: https://github.com/izi-ecommerce/izi-core-stores
.. _izi-core-sagepay-direct: https://github.com/izi-ecommerce/izi-core-sagepay-direct
.. _eWay: https://www.eway.com.au
.. _django_izi_docdata: https://github.com/izi-ecommerce/izi-core-docdata
.. _Docdata: https://www.docdatapayments.com/
.. _django_izi_invoices: https://github.com/izi-ecommerce/izi-core-invoices

The following are community-written extensions:

* izi-core-payments_ - Pluggable payments for IZI
* izi-core-recurly_ - Integration with the Recurly payment gateway

* izi-core-przelewy24_ - Integration with the Przelewy24 payment gateway
* izi-sagepay_ - Payment integration with Sage Pay
* izi-core-erp_
* izi-core-sofortueberweisung_ - Integration with SOFORT

* izi-core-support_ - Customer services and ticketing plugin for IZI

* izi-core-api-checkout_ - IZI API Checkout is a layer on top of
  izi-core and izi-core-api, adding support for more complex and
  multiple payment options during an API checkout.

* izi-core-bundles_ - IZI Bundles adds multi-product bundles to
  izi-core.

* izi-core-bluelight_ - `Bluelight Specials`_ is a layer on-top of
  izi-core that adds support for more complex offers and vouchers,
  including conjunctive and disjunctive compound conditions.

* izi-core-cch_ - IZI CCH is a plugin for izi-core adding support
  for calculating taxes using the Wolters Kluwer `CCH Sales Tax Office`_ SOAP
  API.

* izi-core-cybersource_ - IZI CyberSource is a plugin for IZI API
  Checkout that makes it possible to use
  `CyberSource Secure Acceptance Silent Order Post`_ as an order payment
  method.

* izi-core-wfrs_ - IZI WFRS is a plugin for izi-core-api-checkout_
  that makes it possible to use `Wells Fargo Retail Services`_ as an order
  payment method.

Let us know if you're writing a new one!

.. _izi-core-unicredit: https://bitbucket.org/marsim/izi-core-unicredit/
.. _izi-core-erp: https://bitbucket.org/zikzakmedia/izi-core_erp
.. _izi-core-payments: https://github.com/Lacrymology/izi-core-payments
.. _izi-core-recurly: https://github.com/mynameisgabe/izi-core-recurly

.. _izi-core-przelewy24: https://github.com/kisiel/izi-core-przelewy24
.. _izi-sagepay: https://github.com/udox/izi-sagepay
.. _izi-core-sofortueberweisung: https://github.com/byteyard/izi-core-sofortueberweisung

.. _izi-core-support: https://github.com/SalahAdDin/izi-core-support
.. _izi-core-api-checkout: https://github.com/thelabnyc/izi-core-api-checkout
.. _izi-core-bundles: https://github.com/thelabnyc/izi-core-bundles
.. _izi-core-bluelight: https://github.com/thelabnyc/izi-core-bluelight
.. _`Bluelight Specials`: https://en.wiktionary.org/wiki/blue-light_special
.. _izi-core-cch: https://github.com/thelabnyc/izi-core-cch
.. _`CCH Sales Tax Office`: http://www.salestax.com/solutions/calculation/cch-salestax-office/
.. _izi-core-cybersource: https://github.com/thelabnyc/izi-core-cybersource
.. _`CyberSource Secure Acceptance Silent Order Post`: https://www.cybersource.com/products/payment_security/secure_acceptance_silent_order_post/
.. _izi-core-wfrs: https://github.com/thelabnyc/izi-core-wfrs
.. _`Wells Fargo Retail Services`: https://retailservices.wellsfargo.com/

Videos
------

Videos with talks about IZI:

* `An introduction to Django-izi`_ by `David Winterbottom`_, DjangoCon Europe 2014
* `IZI and the art of transactional Django applications`_ by `David Winterbottom`_, PyCon PL 2014
* `The Tale of IZI and the API`_ by `Kees Hink`_, PyGrunn 2017

.. _`An introduction to Django-izi`: https://youtu.be/o4ol6EzGDSw
.. _`IZI and the art of transactional Django applications`: https://youtu.be/datKUNTKYz8
.. _`The Tale of IZI and the API`: https://youtu.be/YPnKoiyGIHM
.. _`Kees Hink`: https://github.com/khink

License
-------

IZI is released under the permissive `New BSD license`_ (see summary_).

.. _summary: https://tldrlegal.com/license/bsd-3-clause-license-(revised)

.. _`New BSD license`: https://github.com/izi-ecommerce/izi-core/blob/master/LICENSE

Case studies
------------

IZI is still in active development but is used in production by a range of
companies, from large multinationals to small, boutique stores. See
http://ecommerce.izi.asia/cases.html for an overview.

Many more on the way.  If you use IZI in production, please `let us know`_.

.. _`let us know`: https://github.com/izi-core/ecommerce.izi.asia/issues

Looking for commercial support?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are interested in having an IZI project built for you, or for
development of an existing IZI site then please get in touch via `info@ecommerce.izi.asia`_.

.. _`info@ecommerce.izi.asia`: mailto:info@ecommerce.izi.asia
