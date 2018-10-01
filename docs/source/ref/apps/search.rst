======
Search
======

IZI provides a search view that extends Haystack's ``FacetedSearchView`` to
provide better support for faceting.  

* Facets are configured using the ``IZI_SEARCH_FACETS`` setting, which is
  used to configure the ``SearchQuerySet`` instance within the search
  application class.

* A simple search form is injected into each template context using a context
  processor ``izi.apps.search.context_processors.search_form``.

Views
-----

.. automodule:: izi.apps.search.views
    :members:

Forms
-----

.. automodule:: izi.apps.search.forms
    :members:

Utils
-----

.. automodule:: izi.apps.search.facets
    :members:
