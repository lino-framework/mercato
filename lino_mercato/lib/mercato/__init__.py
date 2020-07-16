# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The main plugin for Lino Mercato.

.. autosummary::
   :toctree:

    user_types

"""


from lino.api import ad, _
from itertools import groupby


class Plugin(ad.Plugin):
    "See :class:`lino.core.plugin.Plugin`."

    verbose_name = _("Mercato")

    needs_plugins = ['lino_xl.lib.countries']

    def setup_main_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        #m.add_action('mercato.Clients')

        m.add_action('mercato.Profiles')
        m.add_action('mercato.MyProfiles')

    def setup_config_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        #m.add_action('mercato.LifeModes')

    def setup_explorer_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        #m.add_action('mercato.AllClients')

    def get_dashboard_items(self, user):
        if user.is_authenticated:
            yield self.site.models.mercato.MyProfiles
