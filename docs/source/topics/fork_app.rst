==============
Forking an app
==============

This guide explains how to fork an app in IZI.

.. note::

  The following steps are now automated by the ``izi_fork_app`` management
  command. They're explained in detail so you get an idea of what's going on.
  But there's no need to do this manually anymore! More information is
  available in :ref:`fork-izi-app`.

Create Python module with same label
====================================

You need to create a Python module with the same "app label" as the IZI app
you want to extend. E.g., to create a local version of ``izi.apps.order``,
do the following::

    $ mkdir yourproject/order
    $ touch yourproject/order/__init__.py

Reference IZI's models
========================

If the original IZI app has a ``models.py``, you'll need to create a
``models.py`` file in your local app. It should import all models from
the IZI app being overridden::

    # yourproject/order/models.py

    # your custom models go here

    from izi.apps.order.models import *

If two models with the same name are declared within an app, Django will only
use the first one. That means that if you wish to customise IZI's models, you
must declare your custom ones before importing IZI's models for that app.

You have to copy the ``migrations`` directory from ``izi/apps/order`` and put
it into your ``order`` app. Detailed instructions are available in
:doc:`/howto/how_to_customise_models`.

Get the Django admin working
============================

When you replace one of IZI's apps with a local one, Django admin integration
is lost. If you'd like to use it, you need to create an ``admin.py`` and import
the core app's ``admin.py`` (which will run the register code)::

    # yourproject/order/admin.py
    import izi.apps.order.admin

This isn't great but we haven't found a better way as of yet.

Use supplied app config
=======================

IZI ships with an app config for each app, which sets app labels and
runs startup code. You need to make sure that happens.

.. code-block: django

    # yourproject/order/config.py

    from izi.apps.order import config


    class OrderConfig(config.OrderConfig):
        name = 'yourproject.order'

    # yourproject/order/__init__.py

    default_app_config = 'yourproject.order.config.OrderConfig'
