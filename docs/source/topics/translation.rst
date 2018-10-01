===========
Translation
===========

All IZI translation work is done on Transifex_. If you'd like to contribute,
just apply for a language and go ahead!
The source strings in Transifex are updated after every commit on IZI's
master branch on GitHub. We only pull the translation strings back into IZI's
repository when preparing for a release. That means your most recent
translations will always be on Transifex, not in the repo!

.. _Transifex: https://www.transifex.com/projects/p/izi-core/


Translating IZI within your project
-------------------------------------

If IZI does not provide translations for your language, or if you want to
provide your own, do the following.

Within your project, create a locale folder and a symlink to IZI so that
``./manage.py makemessages`` finds IZI's translatable strings::

    mkdir locale i18n
    ln -s $PATH_TO_IZI i18n/izi
    ./manage.py makemessages --symlinks --locale=de

This will create the message files that you can now translate.
