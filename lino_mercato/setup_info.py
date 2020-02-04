# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

# Note that this module may not have a docstring because any
# global variable defined here will override the global
# namespace of lino/__init__.py who includes it with execfile.

# This module is part of the Lino test suite.
# To test just this module:
#
#   $ python setup.py test -s tests.PackagesTests

SETUP_INFO = dict(
    name='lino_mercato',
    version='0.0.1',
    install_requires=['lino_xl'],
    tests_require=['bleach'],

    description="A Lino application for connecting employers and their future workers",
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
  Operating System :: OS Independent
  Topic :: Database :: Front-Ends
  Topic :: Home Automation
  Topic :: Office/Business""".splitlines())

SETUP_INFO.update(long_description="""\

Lino Mercato is a proof of concept for a company that provides services as a
broker between companies seeking candidates for a job they need to be done and
individual humans who are open to job offers.

The project is in standby mode until we find somebody who wants to invest into
it.

- The central project homepage is http://mercato.lino-framework.org

- For *introductions* and *commercial information* about Lino Mercato
  see http://www.saffre-rumma.net

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
