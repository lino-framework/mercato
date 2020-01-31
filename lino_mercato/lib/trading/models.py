# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


from lino.api import dd, rt, _
from lino.core.utils import ParameterPanel

from lino_xl.lib.contacts.models import *
from lino.modlib.users.mixins import UserAuthored
from .roles import CompanyUser, CandidatUser



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
    # params_layout = "product worker user"
    model = "trading.Offer"
    parameters = ParameterPanel(
        product=dd.ForeignKey("products.Product"),
        company=dd.ForeignKey("contacts.Company",verbose_name=_("Future employer")),
    )
    #required_roles = dd.login_required(CandidatUser)
    insert_layout = """
    product worker
    user
    """
class Needs(dd.Table):
    # params_layout = "product company user"
    model = "trading.Need"
    #required_roles = dd.login_required(CompanyUser)
    parameters = ParameterPanel(
        product=dd.ForeignKey("products.Product"),
        worker=dd.ForeignKey("contacts.Company",verbose_name=_("Future employer")),
    )
    insert_layout = """
    product company
    user
    """

class MyOffers(Offers):
    label = _("My offers")
    @classmethod
    def param_defaults(self, ar, **kw):
        kw = super(Offers, self).param_defaults(ar, **kw)
        kw.update(user=ar.get_user())
        return kw

class MyNeeds(Needs):
    label = _("My needs")
    @classmethod
    def param_defaults(self, ar, **kw):
        kw = super(Needs, self).param_defaults(ar, **kw)
        kw.update(user=ar.get_user())
        return kw

class OffersByWorker(Offers):
    master_key = "worker"

class OffersByProduct(Offers):
    master_key = "product"


class NeedsByCompany(Needs):
    master_key = "company"

class NeedsByProduct(Needs):
    master_key = "product"
