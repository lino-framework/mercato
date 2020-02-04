# -*- coding: UTF-8 -*-
# Copyright 2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Demo data for Lino Mercato.

"""

import datetime
from decimal import Decimal
from django.conf import settings
from django.utils.text import format_lazy

from lino.utils import ONE_DAY
from lino.utils.mti import mtichild
from lino.utils.ssin import generate_ssin
from lino.api import dd, rt, _
from lino.utils import Cycler
from lino.utils import mti
from lino.utils.mldbc import babel_named as named, babeld
from lino.modlib.users.utils import create_user

AMOUNTS = Cycler("5.00", None, None, "15.00", "20.00", None, None)

from lino.utils.quantities import Duration
from lino.core.requests import BaseRequest
from lino_xl.lib.products.choicelists import DeliveryUnits
from lino_xl.lib.ledger.utils import DEBIT, CREDIT
from lino_xl.lib.ledger.choicelists import VoucherStates, JournalGroups
from lino_xl.lib.cal.choicelists import Recurrencies, Weekdays, EntryStates, PlannerColumns

Place = rt.models.countries.Place
Country = rt.models.countries.Country
Role = rt.models.contacts.Role
Partner = rt.models.contacts.Partner
Person = rt.models.contacts.Person
Profile = rt.models.mercato.Profile
User = rt.models.users.User
UserTypes = rt.models.users.UserTypes
Company = rt.models.contacts.Company
Product = rt.models.products.Product
ProductTypes = rt.models.products.ProductTypes
ProductCat = rt.models.products.ProductCat
PriceRule = rt.models.products.PriceRule

def objects():

    # yield skills_objects()

    tallinn = Place.objects.get(name__exact='Tallinn')
    tartu = Place.objects.get(name__exact='Tartu')
    # kettenis = Place.objects.get(name__exact='Kettenis')
    eesti = Country.objects.get(isocode__exact='EE')

    pc_it = named(ProductCat, _("IT"))
    yield pc_it
    pc_metal = named(ProductCat, _("Metal industry"))
    yield pc_metal
    pc_service = named(ProductCat, _("Service industry"))
    yield pc_service
    pc_const = named(ProductCat, _("Construction industry"))
    yield pc_const
    pc_building = named(ProductCat, _("Building"))
    yield pc_building

    obj = Company(
        name="Headhunter OÜ",
        country=eesti, city=tallinn)
    yield obj
    settings.SITE.site_config.update(site_company=obj)

    kw = dict(city=tallinn)
    obj = Company(name="Allways Ltd", **kw)
    yield obj

    kw.update(city=tartu)
    obj = Company(name="Bestbuild Ltd", **kw)
    yield obj
    bernard = Person.objects.get(name__exact="Bodard Bernard")
    adg_dir = Role(company=obj, person=bernard, type_id=1)
    yield adg_dir

    def product(pt, name, pc, **kwargs):
        return Product(**dd.str2kw('name', name,
            cat=pc, product_type=ProductTypes.get_by_name(pt), **kwargs))

    yield product('default', _("Python developer"), pc_it)
    yield product('default', _("Senior Python developer"), pc_it)
    yield product('default', _("React developer"), pc_it)
    yield product('default', _("Java developer"), pc_it)
    yield product('default', _("Blacksmith"), pc_metal)
    yield product('default', _("Carpenter"), pc_building)
    yield product('default', _("Accountant"), pc_service)

    yield create_user("marta", UserTypes.secretary)

    def person2user(p, **kw):
        obj = User(
            user_type=UserTypes.worker, first_name=p.first_name, last_name=p.last_name, partner=p)
        for k, v in kw.items():
            setattr(obj, k, v)
        return obj

    count = 0
    for person in Person.objects.exclude(gender='').exclude(email=''):
        if not person.birth_date:  # not those from humanlinks
            if User.objects.filter(partner=person).count() == 0:
                if rt.models.contacts.Role.objects.filter(person=person).count() == 0:
                    birth_date = settings.SITE.demo_date(-170 * count - 16 * 365)
                    yield person2user(person, birth_date=birth_date, username=person.email)

    # OFFSETS = Cycler(1, 0, 0, 1, 1, 1, 1, 2)
    # START_TIMES = Cycler("8:00", "9:00", "11:00", "13:00", "14:00")
    # DURATIONS = Cycler([Duration(x) for x in ("1:00", "0:30", "2:00", "3:00", "4:00")])
    # USERS = Cycler(User.objects.exclude(user_type=""))
