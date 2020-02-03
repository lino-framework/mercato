# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Defines the user types for Lino Mercato.

"""

from lino.api import _
from lino.modlib.users.choicelists import UserTypes
from lino.core.roles import UserRole, SiteAdmin, SiteUser, SiteStaff
from lino_xl.lib.contacts.roles import ContactsUser, ContactsStaff
from lino_xl.lib.excerpts.roles import ExcerptsUser, ExcerptsStaff
from lino_xl.lib.products.roles import ProductsUser, ProductsStaff
from lino_xl.lib.topics.roles import TopicsUser
from lino_xl.lib.cv.roles import CareerUser, CareerStaff
from lino.modlib.office.roles import OfficeStaff, OfficeUser


class Secretary(SiteStaff, ContactsUser, OfficeUser,
                ExcerptsUser, ProductsStaff, TopicsUser):
    pass


class Worker(SiteUser, ContactsUser, OfficeUser,
                ExcerptsUser, ProductsUser, TopicsUser, CareerUser):
    pass

class Company(SiteUser, ContactsUser, OfficeUser,
                ExcerptsUser,
                ProductsUser, TopicsUser, CareerUser):
    pass

class SiteAdmin(SiteAdmin, ContactsStaff, OfficeStaff,
                ExcerptsStaff, ProductsStaff, TopicsUser, CareerStaff):
    pass

UserTypes.clear()

add = UserTypes.add_item

add('000', _("Anonymous"), UserRole, name='anonymous', readonly=True)
add('100', _("Secretary"), Secretary, name="secretary")
add('200', _("Worker"), Worker, name="worker")
add('300', _("Company"), Company, name="Company")
add('900', _("Administrator"), SiteAdmin, name='admin')
