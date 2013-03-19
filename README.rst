gears-scss
=================

SCSS_ compiler for Gears_.

This package depends on the python ``sass`` module. The ``sass`` module
uses ``libsass``, which unfortunately only supports the ``.scss``
syntax and not the ``.sass`` syntax. Yes, naming in the SASS community
is confusing.

Installation
------------

Install ``gears-scss`` with pip::

    $ pip install gears-scss


Requirements
------------

``gears-scss`` depends on the Python ``sass`` module.


Usage
-----

Add ``gears_scss.SCSSCompiler`` to ``environment``'s compilers registry::

    from gears_scss import SCSSCompiler
    environment.compilers.register('.scss', SCSSCompiler.as_handler())

If you use Gears in your Django project, add this code to its settings::

    GEARS_COMPILERS = {
        '.scss': 'gears_scss.SCSSCompiler',
    }

.. _SCSS: http://sass-lang.org/
.. _Gears: https://github.com/gears/gears