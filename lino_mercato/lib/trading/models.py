# -*- coding: UTF-8 -*-
# Copyright 2013-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


from lino.api import dd, rt, _

from lino_xl.lib.contacts.models import *
from lino_xl.lib.products.models import Product
# from lino_xl.lib.courses.mixins import Enrollable
from lino_xl.lib.beid.mixins import SSIN
from lino_xl.lib.calview.ui import WeeklyColumns
# from lino_xl.lib.calview.ui import WeeklyView
# from lino_xl.lib.calview.ui import WeeklyPlanner
from lino_xl.lib.calview.mixins import Plannable
from lino.modlib.printing.actions import DirectPrintAction
from lino.mixins.periods import Monthly



class Offer(Product):

    class Meta:
        app_label = 'offers'
        verbose_name = _("Offers")
        verbose_name_plural = _("Offers")
        abstract = dd.is_abstract_model(__name__, 'Offer')


class Demand(Product):

    class Meta:
        app_label = 'offers'
        verbose_name = _("Offers")
        verbose_name_plural = _("Offers")
        abstract = dd.is_abstract_model(__name__, 'Offer')


