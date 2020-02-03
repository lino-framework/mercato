# -*- coding: UTF-8 -*-
# Copyright 2013-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


from lino.api import dd, rt, _

from lino_xl.lib.contacts.models import *
from lino_xl.lib.cv.mixins import BiographyOwner


class Partner(Partner, mixins.CreatedModified):

    class Meta(Partner.Meta):
        app_label = 'contacts'
        # verbose_name = _("Partner")
        # verbose_name_plural = _("Partners")
        abstract = dd.is_abstract_model(__name__, 'Partner')

    # isikukood = models.CharField(
    #     _("isikukood"), max_length=20, blank=True)
    #
    hidden_columns = 'created modified'



class PartnerDetail(PartnerDetail):

    main = "general contact misc "

    general = dd.Panel("""
    overview:20 general2:20 general3:40

    """, label=_("General"))

    general2 = """
    id language
    url
    """

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    contact = dd.Panel("""
    address_box
    remarks:30
    """, label=_("Contact"))

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """

    misc = dd.Panel("""
    created modified
    """, label=_("Miscellaneous"))


class Person(Partner, Person):
    """
    Represents a physical person.
    """

    class Meta(Person.Meta):
        app_label = 'contacts'
        # verbose_name = _("Person")
        # verbose_name_plural = _("Persons")
        #~ ordering = ['last_name','first_name']
        abstract = dd.is_abstract_model(__name__, 'Person')

    @classmethod
    def get_user_queryset(cls, user):
        qs = super(Person, cls).get_user_queryset(user)
        return qs.select_related('country', 'city')

    def get_print_language(self):
        "Used by DirectPrintAction"
        return self.language

dd.update_field(Person, 'first_name', blank=False)
# dd.update_field(Person, 'last_name', blank=False)

# class PersonDetail(PersonDetail, PartnerDetail):
class PersonDetail(PartnerDetail):

    main = "general #contact misc"

    general = dd.Panel("""
    overview:20 general2:40 #general3:40 topics.InterestsByPartner:30
    contacts.RolesByPerson:20
    """, label=_("General"))

    # contact = dd.Panel("""
    # remarks:30
    # """, label=_("Contact"))

    misc = dd.Panel("""
    url
    created modified
    # notes.NotesByPartner
    remarks:30
    """, label=_("Miscellaneous"))

    general2 = """
    title first_name:15 middle_name:15
    last_name
    gender:10 birth_date age:10
    id language
    """

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """


Persons.insert_layout = """
first_name last_name
phone gsm
gender email
"""

# class Persons(Persons):
#
#     detail_layout = PersonDetail()


class Worker(Person, BiographyOwner):
    class Meta:
        app_label = 'contacts'
        verbose_name = _("Worker")
        verbose_name_plural = _("Workers")
        abstract = dd.is_abstract_model(__name__, 'Worker')


class WorkerDetail(PersonDetail):

    main = "general contact"

    general = dd.Panel("""
    overview:20 topics.InterestsByPartner:30
    trading.OffersByWorker:50 cv.LanguageKnowledgesByPerson:20
    """, label=_("General"))

    contact = dd.Panel("""
    cv.TrainingsByPerson
    cv.StudiesByPerson
    cv.ExperiencesByPerson
    """, label=_("Career"))




class Workers(Persons):
    model = 'contacts.Worker'
    # detail_layout = WorkerDetail()
    detail_layout = 'contacts.WorkerDetail'


class Company(Partner, Company):
    class Meta(Company.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Company')

    # class Meta:
    #     verbose_name = _("Organisation")
    #     verbose_name_plural = _("Organisations")

    # vat_id = models.CharField(_("VAT id"), max_length=200, blank=True)


class CompanyDetail(PartnerDetail):

    main = "general contact misc"

    general = dd.Panel("""
    overview:20 general2:20 topics.InterestsByPartner:20
    trading.NeedsByCompany
    """, label=_("General"))

    general2 = """
    prefix:20
    name:40
    type
    url
    """

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    contact = dd.Panel("""
    contacts.RolesByCompany:40 general3:40
    remarks:30
    """, label=_("Contact"))

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """

    # tickets = "tickets.SponsorshipsByPartner"

    misc = dd.Panel("""
    id language
    created modified
    # notes.NotesByPartner
    """, label=_("Miscellaneous"))


Companies.insert_layout = """
name
phone gsm
#language:20 email:40
type #id
"""
