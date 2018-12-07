gears-libsass
=================

SCSS_ compiler for Gears_.

This package depends on the python ``libsass`` module. The ``libsass`` module
uses ``libsass``, which unfortunately only supports the ``.scss``
syntax and not the ``.sass`` syntax. Yes, naming in the SASS community
is confusing.

Installation
------------

Install ``gears-libsass`` with pip::

    $ pip install git+https://github.com/wbond/gears-libsass


Requirements
------------

``gears-libsass`` depends on the Python ``libsass`` module.


Usage
-----

Add ``gears_scss.LibsassCompiler`` to ``environment``'s compilers registry::

    from gears_libsass import LibsassCompiler
    environment.compilers.register('.scss', LibsassCompiler.as_handler())

.. _SCSS: http://sass-lang.org/
.. _Gears: https://github.com/gears/gears