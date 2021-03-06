# -*- coding: UTF-8 -*-
# generated by lino.sphinxcontrib.help_text_builder
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

help_texts = {
    'lino_avanti.lib.avanti.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_avanti.lib.avanti.TranslatorTypes' : _("""Types of registries for the Belgian residence."""),
    'lino_avanti.lib.avanti.migrate.Migrator' : _("""The standard migrator for Lino Avanti."""),
    'lino_avanti.lib.users.UserDetail' : _("""Layout of User Detail in Lino Avanti."""),
    'lino_avanti.lib.avanti.Client' : _("""A client is a person using our services."""),
    'lino_avanti.lib.avanti.Client.overview' : _("""A panel with general information about this client."""),
    'lino_avanti.lib.avanti.Client.client_state' : _("""Pointer to ClientStates."""),
    'lino_avanti.lib.avanti.Client.unemployed_since' : _("""The date when this client got unemployed and stopped to have a
regular work."""),
    'lino_avanti.lib.avanti.Client.seeking_since' : _("""The date when this client registered as unemployed and started
to look for a new job."""),
    'lino_avanti.lib.avanti.Client.city' : _("""The place (village or municipality) where this client lives."""),
    'lino_avanti.lib.avanti.Client.municipality' : _("""The municipality where this client lives. This is basically
equal to city, except when city is a village
and has a parent which is a municipality (which causes that
place to be returned)."""),
    'lino_avanti.lib.avanti.Clients' : _("""Base class for most lists of clients."""),
    'lino_avanti.lib.avanti.Clients.client_state' : _("""If not empty, show only Clients whose client_state equals
the specified value."""),
    'lino_avanti.lib.avanti.AllClients' : _("""This table is visible for Explorer who can also export it."""),
    'lino_avanti.lib.avanti.MyClients' : _("""Shows all clients having me as primary coach. Shows all client states."""),
    'lino_avanti.lib.courses.Course' : _("""Same as lino_xl.lib.courses.Course."""),
    'lino_avanti.lib.courses.Enrolment' : _("""Inherits from lino_xl.lib.courses.Enrolment but adds four
specific "enrolment options":"""),
    'lino_avanti.lib.courses.Enrolment.needs_childcare' : _("""Whether this pupil has small children to care about."""),
    'lino_avanti.lib.courses.Enrolment.needs_bus' : _("""Whether this pupil needs public transportation for moving."""),
    'lino_avanti.lib.courses.Enrolment.needs_school' : _("""Whether this pupil has school children to care about."""),
    'lino_avanti.lib.courses.Enrolment.needs_evening' : _("""Whether this pupil is available only for evening courses."""),
    'lino_avanti.lib.courses.PresencesByEnrolment' : _("""Shows the presences of this pupil for this course."""),
    'lino_avanti.lib.courses.EnrolmentsByCourse' : _("""Same as lino_xl.lib.courses.EnrolmentsByCourse but adds
the gender of the pupil (a remote field) and the enrolment
options."""),
    'lino_avanti.lib.courses.Reminder' : _("""A reminder is when a coaching worker sends a written letter to
a client reminding him or her that they have a problme with their
presences."""),
    'lino_avanti.lib.courses.Reminders' : _("""The table of all reminders."""),
    'lino_avanti.lib.courses.RemindersByPupil' : _("""Shows all reminders that have been issued for this pupil."""),
    'lino_avanti.lib.courses.ReminderStates' : _("""The list of possible states of a reminder."""),
    'lino_avanti.lib.courses.EnrolmentChecker' : _("""Checks for the following data problems:"""),
}
