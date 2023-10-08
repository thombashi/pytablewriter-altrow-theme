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

.. image:: https://github.com/thombashi/pytablewriter-altrow-theme/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/thombashi/pytablewriter-altrow-theme/actions/workflows/ci.yml
    :alt: CI status of Linux/macOS/Windows

.. image:: https://coveralls.io/repos/github/thombashi/pytablewriter-altrow-theme/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/pytablewriter-altrow-theme?branch=master
    :alt: Test coverage: coveralls

``pytablewriter-altrow-theme`` is a `pytablewriter <https://github.com/thombashi/pytablewriter>`__ plugin to provide a theme that colored rows alternatively.


Installation
============================================
::

    pip install pytablewriter-altrow-theme

Usage
============================================

:Sample Code:
    .. code-block:: python

        import pytablewriter as ptw

        writer = ptw.TableWriterFactory.create_from_format_name(
            "markdown",
            headers=["INT", "STR"],
            value_matrix=[
                [1, "hoge"],
                [2, "foo"],
                [3, "bar"],
            ],
            margin=1,
            theme="altrow",
        )
        writer.write_table()

:Output:
    .. figure:: https://cdn.jsdelivr.net/gh/thombashi/pytablewriter-altrow-theme@master/ss/ptw-altrow-theme_example_default.png
       :scale: 100%
       :alt: https://github.com/thombashi/pytablewriter-altrow-theme/blob/master/ss/ptw-altrow-theme_example_default.png

You can change the color of the theme by using the ``color`` parameter:

:Sample Code:
    .. code-block:: python

        import pytablewriter as ptw

        writer = ptw.TableWriterFactory.create_from_format_name(
            "markdown",
            headers=["INT", "STR"],
            value_matrix=[
                [1, "hoge"],
                [2, "foo"],
                [3, "bar"],
            ],
            margin=1,
        )

        writer.set_theme("altrow", color="yellow")

        writer.write_table()

:Output:
    .. figure:: https://cdn.jsdelivr.net/gh/thombashi/pytablewriter-altrow-theme@master/ss/ptw-altrow-theme_example_yellow.png
       :scale: 100%
       :alt: https://github.com/thombashi/pytablewriter-altrow-theme/blob/master/ss/ptw-altrow-theme_example_yellow.png


Other Examples
--------------------------------------------
- HTML example: `source file <https://github.com/thombashi/pytablewriter-altrow-theme/blob/master/examples/write_html.py>`__ and `the output <https://thombashi.github.io/pytablewriter-altrow-theme/example.html>`__


Dependencies
============================================
- Python 3.7+
- `Python package dependencies (automatically installed) <https://github.com/thombashi/pytablewriter-altrow-theme/network/dependencies>`__


Related Projects
============================================
- `pytablewriter <https://github.com/thombashi/pytablewriter>`__
- `pytablewriter-altcol-theme <https://github.com/thombashi/pytablewriter-altcol-theme>`__
