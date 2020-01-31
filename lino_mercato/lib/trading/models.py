# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


from lino.api import dd, rt, _

from lino_xl.lib.contacts.models import *
from lino.modlib.users.mixins import UserAuthored



class Offer(UserAuthored):
    # what the person offers
    class Meta:
        app_label = 'trading'
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")
        abstract = dd.is_abstract_model(__name__, 'Offer')

    product = dd.ForeignKey("products.Product")
    worker = dd.ForeignKey("contacts.Worker", verbose_name=_("Future employee"))


class Need(UserAuthored):
    # what the employer needs
    class Meta:
        app_label = 'trading'
        verbose_name = _("Need")
        verbose_name_plural = _("Needs")
        abstract = dd.is_abstract_model(__name__, 'Need')

    product = dd.ForeignKey("products.Product")
    company = dd.ForeignKey("contacts.Company", verbose_name=_("Future employer"))

class Offers(dd.Table):
    params_layout = "product worker"
    model = "trading.Offer"

class Needs(dd.Table):
    params_layout = "product company"
    model = "trading.Need"

class OffersByWorker(Offers):
    master_key = "worker"

class OffersByProduct(Offers):
    master_key = "product"


class NeedsByCompany(Needs):
    master_key = "company"

class NeedsByProduct(Needs):
    master_key = "product"
