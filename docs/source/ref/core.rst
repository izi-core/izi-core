==================
Core functionality
==================

This page details the core classes and functions that IZI uses.  These aren't
specific to one particular app, but are used throughout IZI's codebase.

Dynamic class loading
---------------------

The key to IZI's flexibility is dynamically loading classes.  This allows
projects to provide their own versions of classes that extend and override the
core functionality.

.. automodule:: izi.core.loading
    :members: get_classes, get_class

URL patterns and views
----------------------

IZI's app organise their URLs and associated views using a "Application"
class instance.  This works in a similar way to Django's admin app, and allows
IZI projects to subclass and customised URLs and views.

.. automodule:: izi.core.application
    :members:

Prices
------

IZI uses a custom price object for easier tax handling.

.. automodule:: izi.core.prices
    :members: Price

Custom model fields
-------------------

IZI uses a few custom model fields.

.. automodule:: izi.models.fields
    :members:


Form helpers
------------

.. automodule:: izi.forms.mixins
    :members:
