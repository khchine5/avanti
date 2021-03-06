# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Luc Saffre
# License: BSD (see file COPYING for details)


"""Defines the standard user roles for Lino Avanti."""


from django.utils.translation import ugettext_lazy as _

# from lino.core.roles import UserRole, SiteAdmin, SiteUser
# from lino.core.roles import UserRole, SiteAdmin, SiteStaff
from lino.core.roles import UserRole, Explorer, SiteAdmin, SiteUser
from lino.modlib.users.choicelists import UserTypes
from lino.modlib.comments.roles import CommentsUser, CommentsStaff
from lino.modlib.office.roles import OfficeUser, OfficeStaff, OfficeOperator
from lino.modlib.checkdata.roles import CheckdataUser
from lino.modlib.about.roles import SiteSearcher
from lino_xl.lib.contacts.roles import ContactsUser, ContactsStaff
from lino_xl.lib.cal.roles import GuestOperator
from lino_xl.lib.polls.roles import PollsUser, PollsStaff
from lino_xl.lib.coachings.roles import CoachingsUser, CoachingsStaff
from lino_xl.lib.excerpts.roles import ExcerptsUser, ExcerptsStaff
from lino_xl.lib.courses.roles import CoursesTeacher, CoursesUser
from .roles import ClientsNameUser, ClientsUser, ClientsStaff
from lino_xl.lib.cv.roles import CareerUser, CareerStaff
from lino_xl.lib.beid.roles import BeIdUser
from lino_xl.lib.trends.roles import TrendsStaff, TrendsUser


class Auditor(SiteUser, CoursesUser, OfficeUser, # GuestOperator,
              Explorer):
    pass

class Teacher(SiteUser, CoursesTeacher, OfficeUser, GuestOperator,
              ClientsNameUser):
    pass

class Coordinator(SiteUser, CoursesUser, OfficeOperator,
                  CheckdataUser, ClientsNameUser):
    pass

class Secretary(SiteUser, CoursesUser, OfficeUser, ContactsUser,
                ExcerptsUser, CheckdataUser, ClientsUser):
    pass

class SocialWorker(SiteUser, CoachingsUser, CoursesUser, ContactsUser,
                   OfficeUser, ExcerptsUser, CareerUser, BeIdUser,
                   GuestOperator,
                   CommentsUser, TrendsUser, ClientsUser,
                   Explorer, PollsUser, CheckdataUser):
    pass

class SiteStaff(SocialWorker, CoachingsStaff, CoursesUser,
                ContactsStaff, OfficeStaff, ExcerptsStaff,
                CareerStaff, BeIdUser, #TicketsStaff,
                CommentsStaff, SiteSearcher,
                TrendsStaff, ClientsStaff, Explorer, PollsStaff):
    pass

class Administrator(SiteAdmin, SiteStaff):
    pass

UserTypes.clear()
add = UserTypes.add_item
add('000', _("Anonymous"), UserRole, 'anonymous',
    readonly=True, authenticated=False)
add('100', _("Teacher"), Teacher, name='teacher')
add('200', _("Social worker"), SocialWorker, name='user')
add('300', _("Auditor"), Auditor, name='auditor', readonly=True)
add('400', _("Coordinator"), Coordinator, name='coordinator')
add('410', _("Secretary"), Secretary, name='secretary')
add('800', _("Staff"), SiteStaff, name='staff')
add('900', _("Administrator"), Administrator, name='admin')
