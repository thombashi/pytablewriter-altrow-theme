.. contents:: **pytablewriter-altrow-theme**
   :backlinks: top
   :depth: 2


Summary
============================================

.. image:: https://img.shields.io/travis/thombashi/pytablewriter-altrow-theme/master.svg?label=Linux/macOS%20CI
    :target: https://travis-ci.org/thombashi/pytablewriter-altrow-theme
    :alt: Linux/macOS CI status

.. image:: https://img.shields.io/appveyor/ci/thombashi/pytablewriter-altrow-theme/master.svg?label=Windows%20CI
    :target: https://ci.appveyor.com/project/thombashi/pytablewriter-altrow-theme/branch/master
    :alt: Windows CI status

.. image:: https://coveralls.io/repos/github/thombashi/pytablewriter-altrow-theme/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/pytablewriter-altrow-theme?branch=master
    :alt: Test coverage: coveralls

.. image:: https://codecov.io/gh/thombashi/pytablewriter-altrow-theme/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/thombashi/pytablewriter-altrow-theme
    :alt: Test coverage: codecov

pytablewriter-altrow-theme is a `pytablewriter <https://github.com/thombashi/pytablewriter>`__ plugin to provide a terminal theme.


Installation
============================================
::

    pip install pytablewriter-altrow-theme

Usage
============================================

:Sample Code:
    .. code-block:: python

        writer = TableWriterFactory.create_from_format_name("md")
        writer.headers = ["INT", "STR"]
        writer.value_matrix = [[1, "hoge"], [2, "foo"], [3, "bar"]]
        writer.margin = 1

        writer.set_theme("altrow")

        writer.write_table()

:Output:
    .. figure:: https://cdn.jsdelivr.net/gh/thombashi/pytablewriter-altrow-theme@master/ss/ptw-altrow-theme_example_default.png
       :scale: 100%
       :alt: https://github.com/thombashi/pytablewriter-altrow-theme/blob/master/ss/ptw-altrow-theme_example_default.png


:Sample Code:
    .. code-block:: python

        writer = TableWriterFactory.create_from_format_name("md")
        writer.headers = ["INT", "STR"]
        writer.value_matrix = [[1, "hoge"], [2, "foo"], [3, "bar"]]
        writer.margin = 1

        writer.set_theme("altrow", color="yellow")

        writer.write_table()

:Output:
    .. figure:: https://cdn.jsdelivr.net/gh/thombashi/pytablewriter-altrow-theme@master/ss/ptw-altrow-theme_example_yellow.png
       :scale: 100%
       :alt: https://github.com/thombashi/pytablewriter-altrow-theme/blob/master/ss/ptw-altrow-theme_example_yellow.png

        Specify color to yellow


Dependencies
============================================
- Python 3.5+
- `Python package dependencies (automatically installed) <https://github.com/thombashi/pytablewriter-altrow-theme/network/dependencies>`__

