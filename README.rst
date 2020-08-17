.. contents:: **pytablewriter-altrow-theme**
   :backlinks: top
   :depth: 2


Summary
============================================
.. image:: https://badge.fury.io/py/pytablewriter-altrow-theme.svg
    :target: https://badge.fury.io/py/pytablewriter-altrow-theme
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/pytablewriter-altrow-theme.svg
    :target: https://pypi.org/project/pytablewriter-altrow-theme
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/implementation/pytablewriter-altrow-theme.svg
    :target: https://pypi.org/project/pytablewriter-altrow-theme
    :alt: Supported Python implementations

.. image:: https://github.com/thombashi/pytablewriter-altrow-theme/workflows/Tests/badge.svg
    :target: https://github.com/thombashi/pytablewriter-altrow-theme/actions?query=workflow%3ATests
    :alt: Linux/macOS/Windows CI status

pytablewriter-altrow-theme is a `pytablewriter <https://github.com/thombashi/pytablewriter>`__ plugin to provide a theme that colored rows alternatively.


Installation
============================================
::

    pip install pytablewriter-altrow-theme

Usage
============================================

:Sample Code:
    .. code-block:: python

        writer = TableWriterFactory.create_from_format_name("markdown")
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

        writer = TableWriterFactory.create_from_format_name("markdown")
        writer.headers = ["INT", "STR"]
        writer.value_matrix = [[1, "hoge"], [2, "foo"], [3, "bar"]]
        writer.margin = 1

        writer.set_theme("altrow", color="yellow")

        writer.write_table()

:Output:
    .. figure:: https://cdn.jsdelivr.net/gh/thombashi/pytablewriter-altrow-theme@master/ss/ptw-altrow-theme_example_yellow.png
       :scale: 100%
       :alt: https://github.com/thombashi/pytablewriter-altrow-theme/blob/master/ss/ptw-altrow-theme_example_yellow.png


Dependencies
============================================
- Python 3.5+
- `Python package dependencies (automatically installed) <https://github.com/thombashi/pytablewriter-altrow-theme/network/dependencies>`__

