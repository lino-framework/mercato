# -*- coding: UTF-8 -*-
# Copyright 2017-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import dd, rt, _
from django.db import models
from django.conf import settings

from lino.utils import join_elems
from etgen.html import E

from lino_xl.lib.cv.mixins import BiographyOwner
from lino.modlib.users.mixins import UserAuthored, My
from lino.modlib.publisher.mixins import Publishable
from lino.modlib.publisher.choicelists import PublishableStates
from lino.modlib.memo.mixins import Previewable



class Profile(UserAuthored, BiographyOwner, Publishable, Previewable):
    class Meta:
        app_label = 'mercato'
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        abstract = dd.is_abstract_model(__name__, 'Profile')

    person = dd.ForeignKey("contacts.Person", verbose_name=_("Contact"))
    product = dd.ForeignKey("products.Product")
    title = models.CharField(_("Heading"), max_length=200, blank=True)
    state = PublishableStates.field(default="draft")

    def on_create(self, ar):
        me = ar.get_user()
        self.first_name = me.first_name
        self.last_name = me.last_name
        super(Profile, self).on_create(ar)

class ProfileDetail(dd.DetailLayout):

    main = "general contact"

    general = dd.Panel("""
    person
    overview:20 cv.LanguageKnowledgesByPerson:20
    """, label=_("General"))

    contact = dd.Panel("""
    cv.TrainingsByPerson
    cv.StudiesByPerson
    cv.ExperiencesByPerson
    """, label=_("Career"))




class Profiles(dd.Table):
    model = 'mercato.Profile'
    # detail_layout = WorkerDetail()
    detail_layout = 'mercato.ProfileDetail'

class MyProfiles(My, Profiles):
    column_names = "overview workflow_buttons"
