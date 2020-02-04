.. doctest docs/specs/overview.rst
.. include:: /shared/include/defs.rst

.. _mercato.specs.overview:

========
Overview
========

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_mercato.projects.mercato1.settings.doctests')
>>> from lino.api.doctest import *


Complexity factors
==================

>>> print(analyzer.show_complexity_factors())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 22 plugins
- 33 models
- 13 user roles
- 5 user types
- 98 views
- 7 dialog actions
<BLANKLINE>
