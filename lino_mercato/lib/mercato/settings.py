# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.projects.std.settings import *
from lino.api import _

class Site(Site):
    verbose_name = "Lino Mercato"
    url = "http://mercato.lino-framework.org"
    languages = 'en et'
    demo_fixtures = 'std few_languages demo demo2'
    user_types_module = "lino_mercato.lib.mercato.user_types"

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('topics', 'menu_group', 'contacts')
        yield ('countries', 'country_code', 'BE')
        yield ('cv', 'person_model', 'mercato.Profile')

    def setup_quicklinks(self, user, tb):
        super(Site, self).setup_quicklinks(user, tb)
        tb.add_action(self.models.contacts.Persons)
        tb.add_action(self.models.contacts.Companies)
        # tb.add_action(
        #     self.models.courses.Pupils.insert_action,
        #     label=_("New {}").format(
        #         self.models.courses.Pupil._meta.verbose_name))

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.users'
        yield 'lino_mercato.lib.contacts'
        yield 'lino_mercato.lib.products'
        yield 'lino_mercato.lib.trading'
        yield 'lino_mercato.lib.mercato'
        yield 'lino_xl.lib.topics'
        yield 'lino_xl.lib.cv'
