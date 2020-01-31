# -*- coding: UTF-8 -*-
# Copyright 2019 Rumma & Ko Ltd
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

    verbose_name = _("Master")

    needs_plugins = ['lino_xl.lib.countries']

    municipality_type = '50'

    def setup_main_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        #m.add_action('mercato.Clients')

    def setup_config_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        #m.add_action('mercato.LifeModes')

    def setup_explorer_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        #m.add_action('mercato.AllClients')

    def walk_invoice_entries(self, obj):
        if obj.partner is None or obj.partner.city_id is None:
            return []
        if obj.invoicing_max_date is None:
            return []

        places = set()

        def collect(pl):  # calls itself
            places.add(pl)
            for spl in self.site.models.countries.Place.objects.filter(parent=pl):
                collect(spl)

        collect(obj.partner.city)
        # print("20190506", places)
        qs = self.site.models.cal.Event.objects.filter(
            start_date__lte=obj.invoicing_max_date)
        if obj.invoicing_min_date is not None:
            qs = qs.filter(start_date__gte=obj.invoicing_min_date)
        qs = qs.filter(project__city__in=places)
        # qs = qs.filter(invoicings__voucher__partner__city__in=places)
        qs = qs.filter(state=self.site.models.cal.EntryStates.took_place)
        # qs = qs.filter(**gfk2lookup(obj.__class__.owner, ))
        qs = qs.order_by('project__name', 'start_date', 'start_time')
        return groupby(qs, lambda x: x.project)
