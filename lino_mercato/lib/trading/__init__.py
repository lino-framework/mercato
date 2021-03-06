# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import ad, _


class Plugin(ad.Plugin):
    needs_plugins = ['lino_xl.lib.contacts', 'lino.lib.products']
    # extends_models = ['Partner', 'Person', 'Company']

    # Override to add Workers Menu
    def setup_main_menu(self, site, user_type, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        # We use the string representations and not the classes because
        # other installed applications may want to override these tables.
        m.add_action('trading.Needs')
        m.add_action('trading.MyNeeds')

        # a = site.models.contacts.WorkersWeekly
        # m.add_instance_action(
        #     a.get_row_by_pk(None, "0"), action=a.default_action, label=_("Workers weekly"))
