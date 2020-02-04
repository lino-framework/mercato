# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""See :ref:`mercato`.

.. autosummary::
   :toctree:

   lib
   projects


"""

from os.path import join, dirname

SETUP_INFO = dict()
# execfile(join(dirname(__file__), 'setup_info.py'))
with open(join(dirname(__file__), 'setup_info.py')) as setup_info:
    exec(setup_info.read())
__version__ = SETUP_INFO['version']
# intersphinx_urls = dict(docs="http://mercato.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/mercato/blob/master/%s'
doc_trees = ['docs']
