tw2.slideymenu
==============

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _jQuery UI: http://jqueryui.com/
.. _jQuery: http://jquery.com/
.. _filament group: http://www.filamentgroup.com/

tw2.slideymenu is a `toscawidgets2 (tw2)`_ package with `slidey` menu that I
made just for you!

Live Demo
---------

Slideymenu is best demonstrated by its use in `narcissus
<http://narcissus.rc.rit.edu>`_.  Definitely check it out.

You can also see it in the `tw2 WidgetBrowser
<http://tw2-demos.threebean.org/module?module=tw2.slideymenu>`_ although it doesn't
do it justice.

Links
-----
Get the `source from github <http://github.com/toscawidgets/tw2.slideymenu>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.slideymenu>`_
and `bugs <http://github.com/toscawidgets/tw2.slideymenu/issues/>`_

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

This package contains a menu that slides!

Sampling tw2.slideymenu in the WidgetBrowser
--------------------------------------------

The best way to scope out ``tw2.slideymenu`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.slideymenu/tw2/slideymenu/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.slideymenu.git
    $ cd tw2.slideymenu
    $ mkvirtualenv tw2.slideymenu
    (tw2.slideymenu) $ pip install tw2.devtools
    (tw2.slideymenu) $ python setup.py develop
    (tw2.slideymenu) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
