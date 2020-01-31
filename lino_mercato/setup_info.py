# -*- coding: UTF-8 -*-
# Copyright 2015-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

# Note that this module may not have a docstring because any
# global variable defined here will override the global
# namespace of lino/__init__.py who includes it with execfile.

# This module is part of the Lino test suite.
# To test just this module:
#
#   $ python setup.py test -s tests.PackagesTests

from __future__ import unicode_literals

SETUP_INFO = dict(
    name='lino_mercato',
    version='20.1.0',
    install_requires=['lino_xl'],
    tests_require=['bleach'],

    description="A Lino application for managing tradings",
    license='BSD-2-Clause',
    include_package_data=True,
    zip_safe=False,
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="http://mercato.lino-framework.org",
    #~ test_suite = 'lino.test_apps',
    test_suite='tests',
    classifiers="""\
  Programming Language :: Python
  Programming Language :: Python :: 3
  Development Status :: 4 - Beta
  Environment :: Web Environment
  Framework :: Django
  Intended Audience :: Developers
  Intended Audience :: System Administrators
  License :: OSI Approved :: BSD License
  Natural Language :: English
  Natural Language :: French
  Natural Language :: German
  Operating System :: OS Independent
  Topic :: Database :: Front-Ends
  Topic :: Home Automation
  Topic :: Office/Business""".splitlines())

SETUP_INFO.update(long_description="""\

Lino mercato is an application for managing services with physical
on-site presence of the workers.  For organisations where calendar
entries are the base for writing invoices.  Services can be
individually scheduled or recurring calendar entries based on
contracts.  Integrated calendar and contacts.  Automatically generate
invoices.  Optional functionalities include accounting (payments,
purchases, general ledger, VAT declarations).

- The central project homepage is http://mercato.lino-framework.org

- German documentation is at http://de.mercato.lino-framework.org/

- For *introductions* and *commercial information* about Lino mercato
  see http://www.saffre-rumma.net
  
The name "mercato" originally comes from "prestations de service", the
French expression for service providements.  It also means "quick" in
Italian.

""")

SETUP_INFO.update(packages=[str(n) for n in """
lino_mercato
lino_mercato.lib
lino_mercato.lib.trading
lino_mercato.lib.mercato
lino_mercato.projects
lino_mercato.projects.mercato1
lino_mercato.projects.mercato1.settings
""".splitlines() if n])

SETUP_INFO.update(message_extractors={
    'lino_mercato': [
        ('**/sandbox/**',        'ignore', None),
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**/linoweb.js',        'jinja2', None),
        #~ ('**.js',                'javascript', None),
        ('**/config/**.html', 'jinja2', None),
        #~ ('**/templates/**.txt',  'genshi', {
        #~ 'template_class': 'genshi.template:TextTemplate'
        #~ })
    ],
})

SETUP_INFO.update(package_data=dict())
