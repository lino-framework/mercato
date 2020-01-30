# -*- coding: UTF-8 -*-
# Copyright 2018-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino_presto.lib.presto.settings import *
from lino.api import _

class Site(Site):
    verbose_name = "Lino mercato"
    url = "http://mercato.lino-framework.org"

    languages = 'en de fr'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino_mercato.lib.trading'
