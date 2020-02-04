.. doctest docs/specs/menu.rst
.. include:: /../docs/shared/include/defs.rst

.. _mercato.specs.menu:

========
The menu
========

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_mercato.projects.mercato1.settings.doctests')
>>> from lino.api.doctest import *


>>> rt.login('robin').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Contacts : Persons, Organizations, Profiles, My Profiles
- Trading : Needs, My needs
- Configure :
  - System : Users, Site Parameters, Help Texts
  - Contacts : Organization types, Functions, Topics
  - Products : Jobs, Product Categories, Price rules
  - Career : Education Types, Education Levels, Job Sectors, Job Functions, Work Regimes, Statuses, Contract Durations, Languages
  - Places : Countries, Places
- Explorer :
  - System : Authorities, User types, User roles, content types
  - Contacts : Contact Persons, Partners, Interests
  - Products : Price factors
  - Career : Language knowledges, Trainings, Studies, Job Experiences
- Site : About
