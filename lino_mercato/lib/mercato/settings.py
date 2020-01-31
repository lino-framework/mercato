# -*- coding: UTF-8 -*-
# Copyright 2018-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.projects.std.settings import *
from lino.api import _

class Site(Site):
    verbose_name = "Lino Mercato"
    url = "http://mercato.lino-framework.org"

    languages = 'en et'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino_mercato.lib.contacts'
        yield 'lino_mercato.lib.products'
        yield 'lino_mercato.lib.trading'
        yield 'lino_mercato.lib.mercato'
